
from django.urls import path
from api.views import Class_PeriodListViews, ClassroomListViews, CourseListViews, StudentListViews, TeacherListViews,StudentDetailView, TeacherDetailView, CourseDetailView, ClassroomDetailView, Class_PeriodDetailView , WeeklyTimetable

urlpatterns = [
    path("Students/",StudentListViews.as_view(),name = "student_list_view"),
    path("Teachers/",TeacherListViews.as_view(),name = "teacher_list_view"),
    path("Courses/",CourseListViews.as_view(),name = "course_list_view"),
    path("Classroom/",ClassroomListViews.as_view(),name = "classroom_list_view"),
    path("Class_Period/",Class_PeriodListViews.as_view(),name = "class_period_list_view"),
    path("Students/<int:id>/",StudentDetailView.as_view(), name = "student_detail_view"),
    path("Teachers/<int:id>/",TeacherDetailView.as_view(), name = "teacher_detail_view"),
    path("Courses/<int:id>/",CourseDetailView.as_view(), name = "course_detail_view"),
    path("Classrooms/<int:id>/",ClassroomDetailView.as_view(), name = "classroom_detail_view"),
    path("Class_Periods/<int:id>/",Class_PeriodDetailView.as_view(), name = "class_period_detail_view"),
    path('Weekly-timetable/', WeeklyTimetable.as_view(), name='weekly_timetable'),
]