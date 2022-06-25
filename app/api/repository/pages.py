from typing import Dict


class PageRepository:

    def get_home_content(self) -> Dict:
        return {"message": "Hello my home"}
