from django.db import models
from teacher.models import Teacher

class Courses(models.Model):
    course_id = models.IntegerField()
    course_name = models.CharField(max_length=20)
    course_code = models.PositiveSmallIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    enrolment_capacity = models.PositiveSmallIntegerField()
    department_id = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='courses')
    def __str__(self):
        return f"{self.course_name} {self.course_code}"