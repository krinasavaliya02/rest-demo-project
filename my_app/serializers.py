from .models import Student
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):

    # url = serializers.CharField(
    #     source='get_absolute_url',
    #     read_only=True
    # )
    class Meta:
        model = Student
        fields = '__all__'