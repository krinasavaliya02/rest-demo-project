from .views import *
from django.urls import path

urlpatterns = [
    path('list/', StudentList.as_view(),name='student-list'),
    path('student-detail/<int:pk>/', StudentDetail.as_view()),
]