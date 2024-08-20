from django.db import models
from teacher.models import Teacher
from course.models import Courses

class Classroom(models.Model):
    class_name = models.CharField(max_length=20)
    number_of_seats = models.IntegerField()
    number_of_students = models.IntegerField()
    class_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='classrooms')  
    courses = models.ManyToManyField(Courses, related_name='classrooms')
    available_equipments = models.TextField()
    description = models.TextField()
    def __str__(self):
        return f"{self.class_name}"