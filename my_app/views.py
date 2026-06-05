from rest_framework import generics, mixins, request
from .models import Student
from .serializers import StudentSerializer
from .pagination import MyPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, JSONParser
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, AdminRenderer
from rest_framework.authentication import BasicAuthentication

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

# class StudentList(generics.ListCreateAPIView):

#     queryset = Student.objects.all().order_by('id')

#     serializer_class = StudentSerializer

#     pagination_class = MyPagination
#     filter_backends = [DjangoFilterBackend, OrderingFilter]
#     filterset_fields = ['name', 'city']
#     ordering_fields = ['name']


# class StudentDetail(generics.RetrieveUpdateDestroyAPIView):

#     queryset = Student.objects.all().order_by('id')

#     serializer_class = StudentSerializer


################### model viewset ##################

# class StudentViewSet(viewsets.ModelViewSet):

#     queryset = Student.objects.all().order_by('id')
#     serializer_class = StudentSerializer

#     pagination_class = MyPagination
#     # filter_backends = [DjangoFilterBackend, OrderingFilter]
#     # filterset_fields = ['name', 'city']
#     # ordering_fields = ['name']

#     parser_classes = [JSONParser]

#     renderer_classes = [
#         AdminRenderer,
#         JSONRenderer,
#         BrowsableAPIRenderer
#     ]

##################### Normal viewset ##################

# class StudentList(APIView):

#     def get(self, request):
#         student = Student.objects.all()
#         serializer = StudentSerializer(student, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data, many=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)


# class StudentDetail(APIView):

#     def get(self, request, pk):
#         student = get_object_or_404(Student, pk=pk)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         student = get_object_or_404(Student, pk=pk)
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     def patch(self, request, pk):
#         student = get_object_or_404(Student, pk=pk)
#         serializer = StudentSerializer(student, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     def delete(self, request, pk):
#         student = get_object_or_404(Student, pk=pk)
#         student.delete()
#         return Response({"message": "Deleted successfully"}, status=204)

############## viewsets ##################

class StudentViewSet(viewsets.ViewSet): 
    pagination_class = MyPagination

    # authentication_classes = [BasicAuthentication]
    # print("Authentication classes:", authentication_classes)

    parser_classes = [JSONParser]
    # parser_classes = [FormParser]

    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]

    def list(self, request):

        print("USER:", request.user)
        print("AUTH:", request.auth)
        queryset = Student.objects.all().order_by('id')

        search = request.query_params.get('search')
        if search:
            queryset = queryset.filter(name__icontains=search)

        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)

        serializer = StudentSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    @action(detail=True, methods=['get'])

    def marks(self, request, pk=None):
        return Response({"message": f"Marks of student {pk}"})

    def retrieve(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    # def create(self, request):
    #     print("Request data:", request.data)
    #     serializer = StudentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=400)

    def create(self, request):
        print("Request data:", request.data)
        serializer = StudentSerializer(data=request.data)
        print(serializer.initial_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def update(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student, data=request.data)

        print("INSTANCE:", serializer.instance)
        print("INITIAL DATA:", serializer.initial_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def partial_update(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return Response({"message": "Deleted"})     
    
