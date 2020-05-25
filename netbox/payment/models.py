from django.db import models
from dcim.models import Device
from circuits.models import Circuit
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.urls import reverse
from .choices import PaymentPeriodChoices, PaymentTypeChoices, CurrencyChoices, SubProjectChoices

# Create your models here.
__all__ = (
    'ContractFile',
    'Payment',
)


class ContractFile(models.Model):
    content_type = models.ForeignKey(
        to=ContentType,
        on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField()
    parent = GenericForeignKey(
        ct_field='content_type',
        fk_field='object_id'
    )

    name = models.CharField(
        max_length=30,
        verbose_name='File name'
    )

    document = models.FileField (
        upload_to='devicetype-images'
    )

    created = models.DateTimeField (
        auto_now_add=True
    )

    def __str__(self):
        return self.name
    
        

    class Meta:
        ordering = ['name']


    
class Payment(models.Model):
    name = models.CharField(
        max_length=70,
        verbose_name='Название'
    )

    work_description = models.CharField(
        max_length=150,
        verbose_name='Назначение платежа',
        default=' '
    )

    sub_project = models.CharField(
        max_length=70,
        choices=SubProjectChoices,
        default=SubProjectChoices.STUDIO,
        blank=True
    )



    slug = models.SlugField(
        unique=True
    )

    price = models.IntegerField(
        verbose_name='Стоимость'
    )

    currency = models.CharField(
        max_length=10,
        choices=CurrencyChoices,
        default=CurrencyChoices.DOLLAR,
        verbose_name='Валюта'
    )


    contractor = models.CharField(
        max_length=120,
        verbose_name='Контрагент',
        default=''
    )

    period = models.CharField(
        max_length=50,
        choices=PaymentPeriodChoices,
        default=PaymentPeriodChoices.PAYMENT_MONTH,
        verbose_name='Период'
    )

    payment_type = models.CharField(
        max_length=50,
        choices=PaymentTypeChoices,
        default=PaymentTypeChoices.TYPE_RENT,
        verbose_name='Тип платежа'
    )


    payment_date = models.DateField (
        verbose_name='Дата оплаты',
        auto_now=False,
        auto_now_add=False
    )

    devices = models.ManyToManyField(
        to=Device,
        blank=True,
    )

    circuits = models.ManyToManyField(
        to=Circuit,
        blank=True,
    )

    contract = GenericRelation (
        to='ContractFile'
    )


    comments = models.TextField (
        blank=True
    )
    csv_headers = ['name', 'price', 'period', 'payment_type', 'payment_date', 'comments']

   
    class Meta:
        ordering = ['payment_date', 'name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:payment:payment_view', args=[self.slug])

    def to_csv(self):
        return (
            self.name,
            self.price,
            self.period,
            self.payment_type,
            self.payment_date,
            self.comments   
        )