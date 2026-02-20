from django.urls import path
from . import views

app_name = 'academics'

urlpatterns = [
    path('timetable/manage/', views.manage_timetable, name='manage_timetable'),
    path('timetable/edit/<int:class_id>/', views.edit_timetable, name='edit_timetable'),
    path('timetable/teacher/<int:teacher_id>/', views.edit_timetable_teacher, name='edit_timetable_teacher'),
]

