from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Payment
from students.models import Student
import uuid

@login_required
def initiate_payment(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        student_id = request.POST.get('student_id') # In a real scenario, this would be from the logged in user or session
        
        # Simulate redirect to payment gateway
        return render(request, 'finance/payment_gateway.html', {'amount': amount, 'student_id': student_id})
    return redirect('students:dashboard')

@login_required
def process_payment(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        student_id = request.POST.get('student_id')
        
        try:
            student = Student.objects.get(id=student_id)
            # Create Payment Record
            Payment.objects.create(
                student=student,
                amount_paid=amount,
                transaction_id=str(uuid.uuid4())[:12].upper(),
                remarks="Online Payment"
            )
            messages.success(request, f"Payment of ${amount} successful!")
            return redirect('students:fees')
        except Student.DoesNotExist:
             messages.error(request, "Student not found.")
             
    return redirect('students:dashboard')
