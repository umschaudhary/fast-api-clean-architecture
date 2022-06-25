from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

import os

general_pages_router = InferringRouter()


@cbv(general_pages_router)
class Home:

    directory = os.path.abspath(os.path.expanduser('/app/templates'))
    templates = Jinja2Templates(
        directory=directory
    )

    @general_pages_router.get("/")
    async def index(self, request: Request):
        return self.templates.TemplateResponse("general_pages/homepage.html", {"request": request})

    @general_pages_router.get("/home")
    async def home(self, request: Request):
        return {"message": "Hello World!"}
