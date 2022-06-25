def include_router(api_router, router, prefix, tag):
    """ api/v1 router """

    not_found = {'description': "Not found!"}
    api_router.include_router(
        router,
        prefix=f'/api/v1/{prefix}',
        tags=[tag],
        responses={404: not_found}
    )
