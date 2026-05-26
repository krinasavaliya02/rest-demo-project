from django.db import models
from django.urls import reverse

class Student(models.Model):
    name =  models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('student-detail', args=[self.pk])