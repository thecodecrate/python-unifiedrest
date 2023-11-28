from typing import Optional


class RunnerErrorInterface(Exception):
    def __init__(self, message: Optional[str] = None):
        self.message = message or f"The Runner returned an error"

        super().__init__(self.message)
