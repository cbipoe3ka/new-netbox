from django.contrib import admin

# Register your models here.

from .models import Payment, ContractFile

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'payment_date',
        'comments',

    )

@admin.register(ContractFile)
class ContractFile(admin.ModelAdmin):
    list_display = (
        'name',
        'document',
    )

