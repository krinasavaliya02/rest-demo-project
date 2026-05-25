# from .views import *
# from django.urls import path

# urlpatterns = [
#     path('students/', StudentList.as_view(),name='student-list'),
#     path('student/<int:pk>/', StudentDetail.as_view()),
# ]


from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()
router.register('students', StudentViewSet, basename='student')

urlpatterns = router.urls