from typing import Optional
import os
from datetime import datetime


class IncrementalTracker:
    def __init__(self, last_run_file: str = ".last_run"):
        self.last_run_file = last_run_file
        self.last_run = self._load_last_run()

    def _load_last_run(self) -> Optional[datetime]:
        if os.path.exists(self.last_run_file):
            with open(self.last_run_file, "r") as f:
                timestamp_str = f.read().strip()
                if timestamp_str:
                    return datetime.fromisoformat(timestamp_str)
        return None

    def save_last_run(self):
        with open(self.last_run_file, "w") as f:
            f.write(datetime.utcnow().isoformat())

    def is_new(self, item_date_str: str) -> bool:
        if not self.last_run:
            return True
        try:
            item_date = datetime.fromisoformat(item_date_str.replace("Z", "+00:00"))
            return item_date > self.last_run
        except:
            return True
