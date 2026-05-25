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

    # learned and practiced ViewSet actions and custom routing (@action) in Django REST Framework.
    # learned about routing in Django REST Framework, including SimpleRouter, DefaultRouter, Custom Routers, @action decorator, and DynamicRoute.