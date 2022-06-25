def include_router(app, router, prefix, tag):
    """ api/v1 router """

    not_found = {'description': "Not found!"}
    app.include_router(
        router,
        prefix=f'/api/v1/{prefix}',
        tags=[tag],
        responses={404: not_found}
    )
