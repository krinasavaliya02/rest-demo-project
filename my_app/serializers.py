from .models import Student, Course
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'

 ###########  Validators ###########
 
# def phone_validator(value):
#     if len(value) != 10:
#         raise serializers.ValidationError("Phone must be 10 digits")
    
class StudentSerializer(serializers.ModelSerializer):

    ###########  Validators ###########
    # phone = serializers.CharField(validators=[phone_validator])

    # url = serializers.CharField(
    #     source='get_absolute_url',
    #     read_only=True
    # )

    course = CourseSerializer()
    # course_name = serializers.CharField(source='course.name', read_only=True)

    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        course_data = validated_data.pop('course')
        course = Course.objects.create(**course_data)

        student = Student.objects.create(course=course, **validated_data)
        return student

    ########### Field-level validation ###########

    # def validate_name(self, value):
    #     if len(value) < 3:
    #         raise serializers.ValidationError("Name must be at least 3 characters long.")
    #     return value

    ########### Object-level validation ###########

    # def validate(self, data):
    #     name = data.get('name')
    #     age = data.get('age')

    #     if len(name) < 3 or age < 18:
    #         raise serializers.ValidationError(
    #             "Name must be at least 3 characters and Age must be at least 18"
    #         )

    #     return data

