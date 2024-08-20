from django.db import models
from course.models import Courses
from student.models import Student
from teacher.models import Teacher

class Class_Period(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    start_time = models.TimeField()
    end_time = models.TimeField()  
    course = models.ForeignKey(Courses, on_delete=models.SET_NULL, null=True, related_name='class_periods')
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, related_name='class_periods')  
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='class_periods')  
    day_of_week = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.name