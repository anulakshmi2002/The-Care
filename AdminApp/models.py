from django.db import models

# Create your models here.

class AdminModel(models.Model):
    Admin_id = models.IntegerField(primary_key=True, default=None)
    Admin_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=70)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = "Admin_table"

    def __str__(self):
        return self.Admin_name

class DistrictModel(models.Model):
    District_id = models.IntegerField(primary_key=True, default=None)
    District_Name = models.CharField(max_length=50)

    class Meta:
        db_table = "District_table"

    def __str__(self):
        return self.District_Name


class CityModel(models.Model):
    City_id = models.IntegerField(primary_key=True, default=None)
    City_Name = models.CharField(max_length=50)
    District_id = models.ForeignKey(DistrictModel,on_delete=models.CASCADE)
    class Meta:
        db_table = "City_table"

    def __str__(self):
        return self.City_Name

class HospitalModel(models.Model):
    Hospital_id=models.AutoField(primary_key=True, default=None)
    Hospital_Name=models.CharField(max_length=80)
    Booking_no=models.CharField(max_length=80)
    License_no=models.CharField(max_length=60)
    Hospital_image = models.ImageField(upload_to='image/')
    Password=models.CharField(max_length=60)
    City_id = models.ForeignKey(CityModel, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default="pending")


    class Meta:
        db_table = "Hospital_table"

    def __str__(self):
        return self.Hospital_Name


class DriversModel(models.Model):
    Driver_id=models.IntegerField(primary_key=True, default=None)
    Driver_name=models.CharField(max_length=80)
    Hospital_name=models.CharField(max_length=80)
    images = models.ImageField(upload_to='image/')
    Contact_no=models.CharField(max_length=80)
    City_id = models.ForeignKey(CityModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "Driver_table"

    def __str__(self):
        return self.Driver_name

class DoctorModel(models.Model):
    Doctor_id=models.AutoField(primary_key=True, default=None)
    Doctor_name=models.CharField(max_length=80)
    Department_name=models.CharField(max_length=80)
    images = models.ImageField(upload_to='image/')
    Start_time=models.TimeField()
    End_time=models.TimeField()
    Hospital_id = models.ForeignKey(HospitalModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "DOCTOR_table"

    def __str__(self):
        return self.Doctor_name


class CampModel(models.Model):
    Camp_id=models.AutoField(primary_key=True, default=None)
    Camp_name=models.CharField(max_length=80)
    images = models.ImageField(upload_to='image/')
    Place = models.CharField(max_length=70)
    Start_Date=models.DateTimeField()
    End_Date=models.DateTimeField()
    Doctor_id = models.ForeignKey(DoctorModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "Camp_table"

    def __str__(self):
        return self.Camp_name

class CampregModel(models.Model):
    Register_id = models.AutoField(primary_key=True, default=None)
    Name = models.CharField(max_length=80)
    Phone=models.CharField(max_length=70)
    Place = models.CharField(max_length=70)
    Address=models.CharField(max_length=70)
    Age=models.IntegerField()
    Camp_id = models.ForeignKey(CampModel, on_delete=models.CASCADE)


class Hospitalreg(models.Model):
    Patient_id = models.AutoField(primary_key=True)
    Patient_name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Place = models.CharField(max_length=60)
    Phone = models.CharField(max_length=50,null=True)
    Date =models.CharField(max_length=80,null=True)
    Token =models.IntegerField(null=True)
    Doctor_id = models.ForeignKey(DoctorModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.Patient_name

    class Meta:
        db_table = "HospitalReg_table"


















