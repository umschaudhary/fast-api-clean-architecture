from fastapi import FastAPI, APIRouter
from app.api.v1.controllers import user_router


api_router = APIRouter()


def include_router(router, prefix, tag):
    not_found = {'description': "Not found!"}
    api_router.include_router(
        router,
        prefix=f'/api/v1/{prefix}',
        tags=[tag],
        responses={404: not_found}
    )


include_router(user_router, "users", "Users")
