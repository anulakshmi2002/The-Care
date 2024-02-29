# Generated by Django 5.0.2 on 2024-02-29 08:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminModel',
            fields=[
                ('Admin_id', models.IntegerField(default=None, primary_key=True, serialize=False)),
                ('Admin_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Admin_table',
            },
        ),
        migrations.CreateModel(
            name='CampModel',
            fields=[
                ('Camp_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('Camp_name', models.CharField(max_length=80)),
                ('images', models.ImageField(upload_to='image/')),
                ('Place', models.CharField(max_length=70)),
                ('Start_Date', models.DateTimeField()),
                ('End_Date', models.DateTimeField()),
            ],
            options={
                'db_table': 'Camp_table',
            },
        ),
        migrations.CreateModel(
            name='DistrictModel',
            fields=[
                ('District_id', models.IntegerField(default=None, primary_key=True, serialize=False)),
                ('District_Name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'District_table',
            },
        ),
        migrations.CreateModel(
            name='DoctorModel',
            fields=[
                ('Doctor_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('Doctor_name', models.CharField(max_length=80)),
                ('Department_name', models.CharField(max_length=80)),
                ('images', models.ImageField(upload_to='image/')),
                ('Start_time', models.TimeField()),
                ('End_time', models.TimeField()),
            ],
            options={
                'db_table': 'DOCTOR_table',
            },
        ),
        migrations.CreateModel(
            name='CampregModel',
            fields=[
                ('Register_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=80)),
                ('Phone', models.CharField(max_length=70)),
                ('Place', models.CharField(max_length=70)),
                ('Address', models.CharField(max_length=70)),
                ('Age', models.IntegerField()),
                ('Camp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.campmodel')),
            ],
        ),
        migrations.CreateModel(
            name='CityModel',
            fields=[
                ('City_id', models.IntegerField(default=None, primary_key=True, serialize=False)),
                ('City_Name', models.CharField(max_length=50)),
                ('District_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.districtmodel')),
            ],
            options={
                'db_table': 'City_table',
            },
        ),
        migrations.AddField(
            model_name='campmodel',
            name='Doctor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.doctormodel'),
        ),
        migrations.CreateModel(
            name='DriversModel',
            fields=[
                ('Driver_id', models.IntegerField(default=None, primary_key=True, serialize=False)),
                ('Driver_name', models.CharField(max_length=80)),
                ('Hospital_name', models.CharField(max_length=80)),
                ('images', models.ImageField(upload_to='image/')),
                ('Contact_no', models.CharField(max_length=80)),
                ('City_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.citymodel')),
            ],
            options={
                'db_table': 'Driver_table',
            },
        ),
        migrations.CreateModel(
            name='HospitalModel',
            fields=[
                ('Hospital_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('Hospital_Name', models.CharField(max_length=80)),
                ('Booking_no', models.CharField(max_length=80)),
                ('License_no', models.CharField(max_length=60)),
                ('Hospital_image', models.ImageField(upload_to='image/')),
                ('Password', models.CharField(max_length=60)),
                ('status', models.CharField(default='pending', max_length=50)),
                ('City_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.citymodel')),
            ],
            options={
                'db_table': 'Hospital_table',
            },
        ),
        migrations.AddField(
            model_name='doctormodel',
            name='Hospital_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.hospitalmodel'),
        ),
        migrations.CreateModel(
            name='Hospitalreg',
            fields=[
                ('Patient_id', models.AutoField(primary_key=True, serialize=False)),
                ('Patient_name', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('Place', models.CharField(max_length=60)),
                ('Phone', models.CharField(max_length=50, null=True)),
                ('Doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.doctormodel')),
            ],
            options={
                'db_table': 'HospitalReg_table',
            },
        ),
    ]
