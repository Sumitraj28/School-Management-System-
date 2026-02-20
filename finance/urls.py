from django.urls import path
from . import views

app_name = 'finance'

urlpatterns = [
    path('pay/', views.initiate_payment, name='initiate_payment'),
    path('process/', views.process_payment, name='process_payment'),
]
