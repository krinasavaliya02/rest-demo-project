from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
from .pagination import MyPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

class StudentList(generics.ListCreateAPIView):

    queryset = Student.objects.all().order_by('id')

    serializer_class = StudentSerializer

    pagination_class = MyPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'city']
    ordering_fields = ['name']


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Student.objects.all().order_by('id')

    serializer_class = StudentSerializer