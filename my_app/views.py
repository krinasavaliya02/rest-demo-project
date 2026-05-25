from rest_framework import generics, mixins
from .models import Student
from .serializers import StudentSerializer
from .pagination import MyPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

##################GenericAPIView with mixins ##################
# class StudentList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
   
#     queryset = Student.objects.all().order_by('id')

#     serializer_class = StudentSerializer

#     pagination_class = MyPagination
#     filter_backends = [DjangoFilterBackend, OrderingFilter]
#     filterset_fields = ['name', 'city']
#     ordering_fields = ['name']

#     def get(self, request):
#             return self.list(request)   
    
#     def post(self, request):
#             return self.create(request)


# class StudentDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):

#     queryset = Student.objects.all().order_by('id')

#     serializer_class = StudentSerializer

#     def get(self, request, pk):
#         return self.retrieve(request, pk)       
    
#     def put(self, request, pk):
#         return self.update(request, pk)
    
#     def delete(self, request, pk):
#         return self.destroy(request, pk)
    
################### GenericAPIView  ##################

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



############## viewsets ##################

class StudentViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Student.objects.all().order_by('id')
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        student = Student.objects.get(pk=pk)
        student.delete()
        return Response({"message": "Deleted"})
    

################### model viewset ##################

class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all().order_by('id')
    serializer_class = StudentSerializer

    pagination_class = MyPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'city']
    ordering_fields = ['name']


#####################normal viewset ##################

class StudentList(APIView):

    def get(self, request):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)