from classperiod.models import Class_Period
from classroom.models import Classroom
from course.models import Courses
from student.models import Student
from rest_framework import serializers
from teacher.models import Teacher
from datetime import datetime


class CourseMinimalSerializer(serializers.ModelSerializer):
    duration = serializers.SerializerMethodField()
    class Meta:
        model = Courses
        fields = ['id',  'course_name', 'course_code', 'duration']
    def get_duration(self, obj):
        start_date = obj.start_date
        end_date = obj.end_date
        duration = end_date - start_date
        return duration.days
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"
class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True)
    class Meta:
        model = Student
        exclude = ["email"]
class MinimalStudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_full_name(self, object):
        return f'{object.first_name} {object.last_name}'
    age = serializers.SerializerMethodField()
    def get_age(self, object):
        today = datetime.now().date()
        age = today.year - object.date_of_birth.year - ((today.month, today.day) < (object.date_of_birth.month, object.date_of_birth.day))
        return age
    class Meta:
        model = Student
        fields = ["id", "full_name", "email", "age"]
class TeacherMinimalSerializer(serializers.ModelSerializer):
    courses = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()
    def get_full_name(self, object):
        return f'{object.first_name} {object.last_name}'
    def get_courses(self, obj):
        courses = Courses.objects.filter(teacher=obj)
        return [course.title for course in courses]
    class Meta:
        model = Teacher
        fields = ['id', 'full_name', 'email', 'courses']
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"
class ClassroomMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'class_name', 'description']
class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = "__all__"
class ClassPeriodMinimalSerializer(serializers.ModelSerializer):
    def get_duration(self, obj):
        start_date = obj.start_date
        end_date = obj.end_date
        duration = end_date - start_date
        return duration.days
    class Meta:
        model = Class_Period
        fields = ['id', ' name', 'duration']
class Class_PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class_Period
        fields = '__all__'














