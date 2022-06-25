from typing import Dict
from fastapi import Request
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from app.api.services import PageService

page_router = InferringRouter()


@cbv(page_router)
class Page:
    page_service = PageService()

    @page_router.get("/home")
    def home(self, request: Request) -> Dict:
        return self.page_service.get_home_content()
