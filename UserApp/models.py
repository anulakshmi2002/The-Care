from django.db import models
from AdminApp.models import *



# Create your models here.
class UserModel(models.Model):
    User_id = models.AutoField(primary_key=True,default=None)
    Username = models.CharField(max_length=255)
    Phone_Number = models.CharField(max_length=50)
    Email = models.EmailField(max_length=255)
    Password = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default="Active")

    def __str__(self):
        return self.Username

    class Meta:
        db_table = "User_table"

class UserImageModel(models.Model):
    Image_id = models.AutoField(primary_key=True,default=None)
    Image = models.ImageField(upload_to='image/')
    User_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "UserImage_table"

class DonationCategoryModel(models.Model):
    Category_id = models.IntegerField(primary_key=True,default=None)
    Category_Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Category_Name

    class Meta:
        db_table = "DonationCategory_table"


class FoodModel(models.Model):
    FoodDonation_id = models.AutoField(primary_key=True,default=None)
    Donation_Name = models.CharField(max_length=50)
    Donation_description = models.CharField(max_length=50)
    Start_date =models.DateField(max_length=50)
    End_date =models.DateField(max_length=50)
    Image = models.ImageField(upload_to='image/')
    Category_id = models.ForeignKey(DonationCategoryModel, on_delete=models.CASCADE)
    City_id = models.ForeignKey(CityModel, on_delete=models.CASCADE)


    def __str__(self):
        return self.Donation_Name

    class Meta:
        db_table = "Donation_table"

class Fooddonationreg(models.Model):
    Foodreg_id=models.AutoField(primary_key=True,default=None)
    Id_prooof = models.CharField(max_length=70)
    Id_proofimageee = models.ImageField(upload_to='image/')
    Contact_No = models.CharField(max_length=50)
    Food_item = models.CharField(max_length=60)
    Food_Quantity = models.CharField(max_length=70)
    User_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    City_id = models.ForeignKey(CityModel, on_delete=models.CASCADE)
    FoodDonation_id = models.ForeignKey(FoodModel, on_delete=models.CASCADE)

    status = models.CharField(max_length=50, default="pending")
    class Meta:
        db_table = "Foodreg_table"



class BloodDonationModel(models.Model):
    BloodDonation_id = models.AutoField(primary_key=True,default=None)
    BloodDonation_description = models.CharField(max_length=70)
    Id_proof = models.CharField(max_length=70)
    Id_proofimage = models.ImageField(upload_to='image/')

    Disease=models.CharField(max_length=90)
    Describe=models.CharField(max_length=70)
    Age = models.CharField(max_length=50)
    Gender = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    Blood_group = models.CharField(max_length=50)
    Weight=models.CharField(max_length=70)
    Contact_Number = models.CharField(max_length=50)
    City_id = models.ForeignKey(CityModel, on_delete=models.CASCADE)
    User_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    Category_id = models.ForeignKey(DonationCategoryModel, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default="pending")






    class Meta:
        db_table = "BloodDonation_table"


class PatientModel(models.Model):
    PatientDonation_id = models.AutoField(primary_key=True,default=None)
    Patient_Name = models.CharField(max_length=50)
    Amount = models.CharField(max_length=50)
    Amount_receive=models.CharField(max_length=50)
    Start_date =models.DateField(max_length=50)
    End_date =models.DateField(max_length=50)
    Disease=models.CharField(max_length=60)
    Category_id = models.ForeignKey(DonationCategoryModel, on_delete=models.CASCADE)
    Doctor_id = models.ForeignKey(DoctorModel, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='image/')
    status = models.CharField(max_length=50, default="pending")




    def __str__(self):
        return self.Patient_Name

    class Meta:
        db_table = "Patient_table"







