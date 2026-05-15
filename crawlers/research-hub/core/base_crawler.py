from pathlib import Path
import json
from datetime import datetime
from .api_client import ResearchHubAPIClient
from .incremental import IncrementalTracker


class BaseCrawler:
    def __init__(self, output_dir: str = "output"):
        self.api = ResearchHubAPIClient()
        self.tracker = IncrementalTracker()
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def save_post(self, post_data: dict):
        post_id = post_data.get("@id", post_data.get("id", "unknown")).split("/")[-1]
        post_type = post_data.get("@type", post_data.get("type", "unknown")).replace(
            ":", "_"
        )
        filename = f"{post_type}_{post_id}.json"
        filepath = self.output_dir / filename
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(post_data, f, indent=2, ensure_ascii=False)
        print(f"  Saved: {filename}")

    def run(self):
        raise NotImplementedError
