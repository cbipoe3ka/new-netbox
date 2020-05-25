# Generated by Django 3.0.6 on 2020-05-25 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_payment_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='contractor',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='payment',
            name='currency',
            field=models.CharField(default='USD', max_length=10),
        ),
        migrations.AddField(
            model_name='payment',
            name='sub_project',
            field=models.CharField(blank=True, default='Студия', max_length=70),
        ),
        migrations.AddField(
            model_name='payment',
            name='work_description',
            field=models.CharField(default=' ', max_length=150),
        ),
    ]