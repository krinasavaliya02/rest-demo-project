from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("users", views.UserViewSet , basename="users")
router.register("groups", views.GroupViewSet , basename="groups")


urlpatterns = router.urls