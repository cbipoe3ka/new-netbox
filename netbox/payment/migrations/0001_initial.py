# Generated by Django 3.0.6 on 2020-05-25 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('work_description', models.CharField(default=' ', max_length=150)),
                ('sub_project', models.CharField(blank=True, default='Студия', max_length=70)),
                ('slug', models.SlugField(unique=True)),
                ('price', models.IntegerField()),
                ('currency', models.CharField(default='USD', max_length=10)),
                ('period', models.CharField(default='monthly', max_length=50)),
                ('payment_type', models.CharField(default='Rent', max_length=50)),
                ('payment_date', models.DateField()),
                ('comments', models.TextField(blank=True)),
                ('circuits', models.ManyToManyField(blank=True, to='circuits.Circuit')),
                ('comp', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='payment.Company')),
                ('contractor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='payment.Contractor')),
                ('devices', models.ManyToManyField(blank=True, to='dcim.Device')),
            ],
            options={
                'ordering': ['payment_date', 'name'],
            },
        ),
        migrations.CreateModel(
            name='ContractFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('object_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=30)),
                ('document', models.FileField(upload_to='devicetype-images')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
