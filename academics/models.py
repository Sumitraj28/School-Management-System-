from django.conf import settings
from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=5)
    teacher = models.ForeignKey('staff.Staff', on_delete=models.SET_NULL, null=True, blank=True, related_name='class_teacher')

    class Meta:
        unique_together = ('name', 'section')
        verbose_name_plural = "Classes"

    def __str__(self):
        return f"{self.name} - {self.section}"

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    classes = models.ManyToManyField(Class, related_name='subjects')
    teacher = models.ForeignKey('staff.Staff', on_delete=models.SET_NULL, null=True, blank=True, related_name='subjects_taught')
    
    def __str__(self):
        return f"{self.name} ({self.code})"

class Exam(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='exams')
    class_group = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='exams')
    total_marks = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.subject} ({self.class_group})"

class Grade(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE, related_name='grades')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='grades')
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    remarks = models.TextField(blank=True)

    class Meta:
        unique_together = ('student', 'exam')

    def __str__(self):
        return f"{self.student} - {self.exam}: {self.marks_obtained}"

class Attendance(models.Model):
    class Status(models.TextChoices):
        PRESENT = 'PRESENT', 'Present'
        ABSENT = 'ABSENT', 'Absent'
        LATE = 'LATE', 'Late'
        EXCUSED = 'EXCUSED', 'Excused'

    student = models.ForeignKey('students.Student', on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=Status.choices)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student} - {self.date} ({self.status})"

class Timetable(models.Model):
    class DayOfWeek(models.TextChoices):
        MONDAY = 'MONDAY', 'Monday'
        TUESDAY = 'TUESDAY', 'Tuesday'
        WEDNESDAY = 'WEDNESDAY', 'Wednesday'
        THURSDAY = 'THURSDAY', 'Thursday'
        FRIDAY = 'FRIDAY', 'Friday'
        SATURDAY = 'SATURDAY', 'Saturday'
        SUNDAY = 'SUNDAY', 'Sunday'

    class_group = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='timetable')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey('staff.Staff', on_delete=models.SET_NULL, null=True, blank=True)
    day = models.CharField(max_length=10, choices=DayOfWeek.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_number = models.CharField(max_length=20, blank=True)

    class Meta:
        unique_together = ('class_group', 'day', 'start_time')

    def __str__(self):
        return f"{self.class_group} - {self.day} {self.start_time} ({self.subject})"

class Homework(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='homeworks')
    class_group = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='homeworks')
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_date = models.DateField()
    due_date = models.DateField()
    assigned_by = models.ForeignKey('staff.Staff', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.subject} ({self.class_group})"
