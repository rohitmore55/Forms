from django.db import models

class DefaultFormData(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    CLASS_CHOICES = (
        ('A', 'Class A'),
        ('B', 'Class B'),
        ('C', 'Class C'),
    )
    class_field = models.CharField(max_length=1, choices=CLASS_CHOICES)

class EditedFormData(models.Model):
    field_name = models.CharField(max_length=100)
    field_value = models.CharField(max_length=100)

