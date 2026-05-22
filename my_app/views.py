from rest_framework import generics, mixins
from .models import Student
from .serializers import StudentSerializer
from .pagination import MyPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

class StudentList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
   
    queryset = Student.objects.all().order_by('id')

    serializer_class = StudentSerializer

    pagination_class = MyPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'city']
    ordering_fields = ['name']

    def get(self, request):
            return self.list(request)   
    
    def post(self, request):
            return self.create(request)


class StudentDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):

    queryset = Student.objects.all().order_by('id')

    serializer_class = StudentSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)       
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)