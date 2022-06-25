from app.api.repository import PageRepository


class PageService:
    page_repo = PageRepository()

    def get_home_content(self):
        return self.page_repo.get_home_content()
