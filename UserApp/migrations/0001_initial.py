# Generated by Django 5.0.2 on 2024-02-29 08:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AdminApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonationCategoryModel',
            fields=[
                ('Category_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Category_Name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'DonationCategory_table',
            },
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('User_id', models.AutoField(primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=255)),
                ('Phone_Number', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=255)),
                ('Password', models.CharField(max_length=255)),
                ('status', models.CharField(default='Active', max_length=50)),
            ],
            options={
                'db_table': 'User_table',
            },
        ),
        migrations.CreateModel(
            name='UserImageModel',
            fields=[
                ('Image_id', models.AutoField(primary_key=True, serialize=False)),
                ('Image', models.ImageField(upload_to='image/')),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.usermodel')),
            ],
            options={
                'db_table': 'UserImage_table',
            },
        ),
        migrations.CreateModel(
            name='PatientModel',
            fields=[
                ('PatientDonation_id', models.AutoField(primary_key=True, serialize=False)),
                ('Patient_Name', models.CharField(max_length=50)),
                ('Amount', models.CharField(max_length=50)),
                ('Amount_receive', models.CharField(max_length=50)),
                ('Start_date', models.DateField(max_length=50)),
                ('End_date', models.DateField(max_length=50)),
                ('Image', models.ImageField(upload_to='image/')),
                ('Contact_Number', models.CharField(max_length=50)),
                ('status', models.CharField(default='pending', max_length=50)),
                ('Category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.donationcategorymodel')),
                ('Doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.doctormodel')),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.usermodel')),
            ],
            options={
                'db_table': 'Patient_table',
            },
        ),
        migrations.CreateModel(
            name='FoodModel',
            fields=[
                ('FoodDonation_id', models.AutoField(primary_key=True, serialize=False)),
                ('Donation_Name', models.CharField(max_length=50)),
                ('Donation_description', models.CharField(max_length=50)),
                ('Start_date', models.DateField(max_length=50)),
                ('End_date', models.DateField(max_length=50)),
                ('Image', models.ImageField(upload_to='image/')),
                ('Id_proof', models.CharField(max_length=70)),
                ('Id_proofimage', models.ImageField(upload_to='image/')),
                ('Contact_Number', models.CharField(max_length=50)),
                ('Quantity', models.CharField(max_length=70)),
                ('status', models.CharField(default='pending', max_length=50)),
                ('Category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.donationcategorymodel')),
                ('City_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.citymodel')),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.usermodel')),
            ],
            options={
                'db_table': 'Donation_table',
            },
        ),
        migrations.CreateModel(
            name='BloodDonationModel',
            fields=[
                ('BloodDonation_id', models.AutoField(primary_key=True, serialize=False)),
                ('BloodDonation_description', models.CharField(max_length=70)),
                ('Id_proof', models.CharField(max_length=70)),
                ('Id_proofimage', models.ImageField(upload_to='image/')),
                ('Disease', models.CharField(max_length=90)),
                ('Describe', models.CharField(max_length=70)),
                ('Age', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=50)),
                ('Blood_group', models.CharField(max_length=50)),
                ('Weight', models.CharField(max_length=70)),
                ('Contact_Number', models.CharField(max_length=50)),
                ('status', models.CharField(default='pending', max_length=50)),
                ('City_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.citymodel')),
                ('Category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.donationcategorymodel')),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.usermodel')),
            ],
            options={
                'db_table': 'BloodDonation_table',
            },
        ),
    ]
