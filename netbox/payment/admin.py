from django.contrib import admin

# Register your models here.

from .models import Payment, ContractFile, Company, Contractor

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


@admin.register(Company)
class Company(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(Contractor)
class Contractor(admin.ModelAdmin):
    list_display = (
        'name',
    )