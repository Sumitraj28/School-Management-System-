from django import forms
from django.contrib import admin
from .models import Class, Subject, Exam, Grade, Attendance, Timetable

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'section', 'teacher')
    list_filter = ('name',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'teacher')
    search_fields = ('name', 'code')

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    form = ExamForm
    list_display = ('name', 'subject', 'class_group', 'date', 'total_marks')
    list_filter = ('class_group', 'subject', 'date')

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam', 'marks_obtained')
    list_filter = ('exam__class_group', 'exam__subject')
    search_fields = ('student__user__username',)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    form = AttendanceForm
    list_display = ('student', 'date', 'status')
    list_filter = ('date', 'status', 'student__current_class')
    search_fields = ('student__user__username',)

@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('class_group', 'day', 'start_time', 'end_time', 'subject', 'teacher')
    list_filter = ('class_group', 'day', 'teacher')

