from django.contrib import admin
from .models import FeeStructure, Payment, Invoice

@admin.register(FeeStructure)
class FeeStructureAdmin(admin.ModelAdmin):
    list_display = ('class_level', 'academic_year', 'tuition_fee', 'other_fees')
    list_filter = ('academic_year', 'class_level')

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'student', 'amount_due', 'due_date', 'is_paid')
    list_filter = ('is_paid', 'due_date')
    search_fields = ('invoice_number', 'student__user__username')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('student', 'amount_paid', 'payment_method', 'payment_date', 'transaction_id')
    search_fields = ('student__admission_number', 'transaction_id')
    list_filter = ('payment_date', 'payment_method')
