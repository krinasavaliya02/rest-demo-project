# from .views import *
# from django.urls import path

# urlpatterns = [
#     path('students/', StudentList.as_view(),name='student-list'),
#     path('students/<int:pk>/', StudentDetail.as_view()),
# ]


from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import StudentViewSet

router = DefaultRouter()
# router = SimpleRouter(use_regex_path=False)
router.register('students', StudentViewSet, basename='student')

urlpatterns = router.urls
print("URL patterns:", router.urls)

# from .routers import MyCustomRouter
# from .views import StudentViewSet

# router = MyCustomRouter()
# router.register('students', StudentViewSet, basename='student')

# urlpatterns = router.urls
# print("URL patterns:", router.urls)