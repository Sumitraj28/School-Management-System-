from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from core.models import User
from .models import Class, Timetable, Subject
from staff.models import Staff

def is_admin(user):
    return user.is_authenticated and user.role == User.Role.ADMIN

@login_required
@user_passes_test(is_admin)
def manage_timetable(request):
    classes = Class.objects.all().order_by('name', 'section')
    teachers = Staff.objects.select_related('user').all().order_by('user__first_name')
    
    # Count timetable entries per class and teacher
    for cls in classes:
        cls.entry_count = Timetable.objects.filter(class_group=cls).count()
    
    for teacher in teachers:
        teacher.entry_count = Timetable.objects.filter(teacher=teacher).count()
    
    context = {
        'classes': classes,
        'teachers': teachers,
    }
    return render(request, 'academics/manage_timetable.html', context)

@login_required
@user_passes_test(is_admin)
def edit_timetable(request, class_id):
    class_obj = get_object_or_404(Class, id=class_id)
    timetable_entries = Timetable.objects.filter(class_group=class_obj).order_by('day', 'start_time')
    
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'add':
            subject_id = request.POST.get('subject')
            teacher_id = request.POST.get('teacher')
            day = request.POST.get('day')
            start_time = request.POST.get('start_time')
            end_time = request.POST.get('end_time')
            room = request.POST.get('room_number', '')
            
            subject = get_object_or_404(Subject, id=subject_id)
            teacher = get_object_or_404(Staff, id=teacher_id) if teacher_id else None
            
            Timetable.objects.create(
                class_group=class_obj,
                subject=subject,
                teacher=teacher,
                day=day,
                start_time=start_time,
                end_time=end_time,
                room_number=room
            )
            messages.success(request, "Timetable entry added successfully.")
            
        elif action == 'delete':
            entry_id = request.POST.get('entry_id')
            entry = get_object_or_404(Timetable, id=entry_id)
            entry.delete()
            messages.success(request, "Timetable entry deleted.")
            
        return redirect('academics:edit_timetable', class_id=class_id)

    subjects = Subject.objects.all()
    teachers = Staff.objects.all()
    days = Timetable.DayOfWeek.choices
    
    context = {
        'class': class_obj,
        'timetable': timetable_entries,
        'subjects': subjects,
        'teachers': teachers,
        'days': days,
    }
    return render(request, 'academics/edit_timetable.html', context)


@login_required
@user_passes_test(is_admin)
def edit_timetable_teacher(request, teacher_id):
    teacher_obj = get_object_or_404(Staff, id=teacher_id)
    timetable_entries = Timetable.objects.filter(teacher=teacher_obj).order_by('day', 'start_time')
    
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'add':
            class_id = request.POST.get('class_group')
            subject_id = request.POST.get('subject')
            day = request.POST.get('day')
            start_time = request.POST.get('start_time')
            end_time = request.POST.get('end_time')
            room = request.POST.get('room_number', '')
            
            class_obj = get_object_or_404(Class, id=class_id)
            subject = get_object_or_404(Subject, id=subject_id)
            
            Timetable.objects.create(
                class_group=class_obj,
                subject=subject,
                teacher=teacher_obj,
                day=day,
                start_time=start_time,
                end_time=end_time,
                room_number=room
            )
            messages.success(request, f"Timetable slot added for {teacher_obj.user.get_full_name()}.")
            
        elif action == 'delete':
            entry_id = request.POST.get('entry_id')
            entry = get_object_or_404(Timetable, id=entry_id)
            entry.delete()
            messages.success(request, "Timetable entry deleted.")
            
        return redirect('academics:edit_timetable_teacher', teacher_id=teacher_id)

    classes = Class.objects.all().order_by('name', 'section')
    subjects = Subject.objects.all()
    days = Timetable.DayOfWeek.choices
    
    context = {
        'teacher': teacher_obj,
        'timetable': timetable_entries,
        'classes': classes,
        'subjects': subjects,
        'days': days,
    }
    return render(request, 'academics/edit_timetable_teacher.html', context)
