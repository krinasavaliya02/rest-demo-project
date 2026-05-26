from rest_framework.routers import DefaultRouter, Route

class MyCustomRouter(DefaultRouter):
    routes = [
        Route(
            url=r'^{prefix}/$',
            mapping={
                'get': 'list',
                'post': 'create'
            },
            name='{basename}-list',
            detail=False,
            initkwargs={}
        ),
    ]

