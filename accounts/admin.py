# accounts/admin.py
from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'table_number', 'person_name', 'created_at')
