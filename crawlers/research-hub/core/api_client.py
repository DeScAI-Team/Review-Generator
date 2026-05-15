import requests
import time
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime

logger = logging.getLogger(__name__)


class ResearchHubAPIClient:
    BASE_URL = "https://backend.prod.researchhub.com/api"

    def __init__(self, timeout: int = 30, delay: float = 0.5, max_retries: int = 3):
        self.timeout = timeout
        self.delay = delay
        self.max_retries = max_retries
        self.session = requests.Session()
        self.last_request_time = 0
        self.request_count = 0
        self.daily_limit = 10000
        self.reset_time = datetime.now().date()

    def _respect_rate_limit(self):
        elapsed = time.time() - self.last_request_time
        if elapsed < self.delay:
            time.sleep(self.delay - elapsed)
        if datetime.now().date() > self.reset_time:
            self.request_count = 0
            self.reset_time = datetime.now().date()
        if self.request_count >= self.daily_limit:
            logger.warning("Daily API limit reached. Waiting...")
            time.sleep(3600)
            self.request_count = 0
        self.last_request_time = time.time()

    def get_paginated(
        self,
        endpoint: str,
        params: Optional[Dict] = None,
        max_pages: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        if params is None:
            params = {}
        params.setdefault("page_size", 100)

        all_results = []
        page = 1
        pages_fetched = 0

        while True:
            if max_pages and pages_fetched >= max_pages:
                break
            params["page"] = page
            url = f"{self.BASE_URL}{endpoint}"
            self._respect_rate_limit()
            for attempt in range(self.max_retries):
                try:
                    response = self.session.get(
                        url, params=params, timeout=self.timeout
                    )
                    self.request_count += 1
                    if response.status_code == 429:
                        wait_time = 60 * (attempt + 1)
                        time.sleep(wait_time)
                        continue
                    response.raise_for_status()
                    data = response.json()
                    results = data.get("results", [])
                    all_results.extend(results)
                    if not data.get("next"):
                        return all_results
                    page += 1
                    pages_fetched += 1
                    break
                except requests.exceptions.RequestException as e:
                    if attempt == self.max_retries - 1:
                        logger.error(f"Failed after {self.max_retries} attempts: {e}")
                        raise
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                    time.sleep(5 * (attempt + 1))
        return all_results

    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        self._respect_rate_limit()
        url = f"{self.BASE_URL}{endpoint}"
        for attempt in range(self.max_retries):
            try:
                response = self.session.get(url, params=params, timeout=self.timeout)
                self.request_count += 1
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                if attempt == self.max_retries - 1:
                    logger.error(f"Failed after {self.max_retries} attempts: {e}")
                    raise
                logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                time.sleep(5 * (attempt + 1))
