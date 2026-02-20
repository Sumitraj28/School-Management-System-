from django.core.management.base import BaseCommand
from core.models import User
from students.models import Student, Parent
from staff.models import Staff
from academics.models import Class, Subject, Exam
from finance.models import FeeStructure
from django.utils import timezone
import datetime
import random

class Command(BaseCommand):
    help = 'Populates the database with dummy data for testing'

    def handle(self, *args, **kwargs):
        self.stdout.write("Populating data...")

        # 1. Create Teacher
        teacher_user, created = User.objects.get_or_create(
            username='teacher_demo',
            email='teacher_demo@example.com',
            defaults={'role': User.Role.TEACHER, 'first_name': 'Sarah', 'last_name': 'Connor'}
        )
        if created:
            teacher_user.set_password('password123')
            teacher_user.save()
            self.stdout.write(self.style.SUCCESS(f"Created Teacher: {teacher_user.username}"))
        
        staff, _ = Staff.objects.get_or_create(
            user=teacher_user,
            defaults={
                'designation': 'Class Teacher',
                'employee_id': 'EMP_D001',
                'department': 'Science',
                'joining_date': datetime.date(2023, 1, 1)
            }
        )

        # 2. Create Class
        class_obj, class_created = Class.objects.get_or_create(
            name='Class 5',
            section='A',
            defaults={'teacher': staff}
        )
        if class_created:
            self.stdout.write(self.style.SUCCESS(f"Created Class: {class_obj}"))

        # 3. Create Multiple Students
        first_names = ["Emma", "Liam", "Olivia", "Noah", "Ava", "William", "Sophia", "James", "Isabella", "Benjamin"]
        last_names = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin"]

        for i in range(10):
            fname = first_names[i]
            lname = last_names[i]
            username = f'student_demo_{i+1}'
            email = f'{username}@example.com'
            adm_no = f'ADM_D00{i+1}'

            user, created = User.objects.get_or_create(
                username=username,
                email=email,
                defaults={'role': User.Role.STUDENT, 'first_name': fname, 'last_name': lname}
            )
            
            if created:
                user.set_password('password123')
                user.save()
                
                Student.objects.create(
                    user=user,
                    admission_number=adm_no,
                    date_of_birth=datetime.date(2015, 1, 1),
                    address=f'{random.randint(1,999)} Demo Street',
                    current_class=class_obj
                )
                self.stdout.write(f"Created Student: {fname} {lname} ({username})")

        # 4. Create Subject & Assign to Class
        subject, _ = Subject.objects.get_or_create(
            name='Mathematics',
            code='MATH501',
            defaults={'teacher': staff}
        )
        subject.classes.add(class_obj)
        
        self.stdout.write(self.style.SUCCESS('Successfully populated dummy student data!'))
        self.stdout.write(self.style.WARNING("--------------------------------------------------"))
        self.stdout.write(self.style.SUCCESS('Log in as Teacher with:'))
        self.stdout.write(self.style.SUCCESS('Username: teacher_demo'))
        self.stdout.write(self.style.SUCCESS('Password: password123'))
        self.stdout.write(self.style.WARNING("--------------------------------------------------"))
