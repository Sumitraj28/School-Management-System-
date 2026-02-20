from django.db import models
from students.models import Student
import uuid

class FeeStructure(models.Model):
    class_level = models.ForeignKey('academics.Class', on_delete=models.CASCADE)
    tuition_fee = models.DecimalField(max_digits=10, decimal_places=2)
    other_fees = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    academic_year = models.CharField(max_length=9)  # E.g., "2023-2024"

    def total_fee(self):
        return self.tuition_fee + self.other_fees

    def __str__(self):
        return f"Fee Structure for {self.class_level} ({self.academic_year})"


class Invoice(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee_structure = models.ForeignKey(FeeStructure, on_delete=models.SET_NULL, null=True)
    date_issued = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    invoice_number = models.CharField(max_length=20, unique=True, default=uuid.uuid4)

    def __str__(self):
        return f"Invoice {self.invoice_number} for {self.student}"

class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, on_delete=models.SET_NULL, null=True, blank=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    payment_method = models.CharField(max_length=50, default='CASH') # CASH, ONLINE, CHEQUE
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"Payment of {self.amount_paid} by {self.student}"
