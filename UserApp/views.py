from django.shortcuts import render, redirect
from django.db.models import Q
from AdminApp.models import *
from UserApp.models import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate
from django.db import IntegrityError


# Create your views here.
def Home(request):
    return render(request, 'Home.html')


def Signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        exists = UserModel.objects.filter(Username=username).exists()

        if exists:

            return redirect('sign')
        else:
            user = UserModel(Username=username, Email=email, Phone_Number=phone, Password=password)
            user.save()

            return redirect('login')
    return render(request, "Signup.html")


def Driver(request):
    if request.method == "POST":
        search = request.POST.get('city')
        data = DriversModel.objects.filter(City_id=CityModel.objects.get(City_Name=search))
        return render(request, 'Driver.html', {'data': data})
    return render(request, 'Driver.html')


def Hospital(request):


    if request.method == "POST":
        search = request.POST.get('cityname')
        # dataaa = HospitalModel.objects.filter(City_id=CityModel.objects.get(City_Name=search))
        dataaa = HospitalModel.objects.filter(Q(Hospital_Name__icontains=search) | Q(City_id__City_Name__icontains=search) |
                                              Q(City_id__District_id__District_Name__icontains=search))


        # searchh = request.POST.get('search')
        # if search:
        #     sear = HospitalModel.objects.filter(Q(Hospital_Name__icontains=searchh) | Q(City_id__District_id__icontains=searchh))
        #     print(search)

        return render(request, 'Hospital.html', {'data': dataaa})
    return render(request, 'Hospital.html')


def Doctor(request, id):
    data = DoctorModel.objects.filter(Hospital_id=HospitalModel.objects.get(Hospital_id=id))
    if request.method == "POST":
        search = request.POST.get('cityname')
        # dataaa = HospitalModel.objects.filter(City_id=CityModel.objects.get(City_Name=search))
        dataa = DoctorModel.objects.filter(Q(Doctor_name__icontains=search)| Q( Department_name__icontains=search) )


        return render(request, 'Doctor.html', {'data': dataa})
    return render(request, 'Doctor.html',{'data':data})



def Camp(request):
    data = CampModel.objects.all()
    return render(request, 'Camp.html', {'data': data})


def campreg(request, id):
    data = CampModel.objects.filter(Camp_id=id)
    return render(request, 'Campdetail.html', {'data': data})


def campregistration(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        age = request.POST.get('age')
        place = request.POST.get('place')
        Camp_id = CampModel.objects.get(Camp_id=id)
        data = CampregModel(Name=name, Phone=phone, Address=address, Age=age, Place=place, Camp_id=Camp_id)

        data.save()
        return redirect('camp')
    return render(request, 'Campreg.html')


# def sign(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         password = request.POST.get('password')
#
#         exists = UserModel.objects.filter(Username=username).exists()
#         if exists:
#             messages.error(request, 'number already exits')
#             return redirect('sign')
#         else:
#             data = UserModel(Username=username, Phone_Number=phone, Email=email, Password=password)
#             data.save()
#             return redirect('login')
#     return render(request, 'Signup.html')
#
def sign(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        exists = UserModel.objects.filter(Username=username).exists()
        if exists:
            messages.error(request, 'Username already exists.')
            return redirect('sign')
        else:
            data = UserModel(Username=username, Phone_Number=phone, Email=email, Password=password)
            data.save()
            return redirect('login')
    else:
        # Get any error messages that were added to the request
        error_messages = messages.get_messages(request)
        return render(request, 'Signup.html', {'error_messages': error_messages})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        check_user = UserModel.objects.filter(Username=username, Password=password)
        if check_user:

            request.session['user'] = username

            return redirect('home')
        else:
            return HttpResponse('Please enter valid Username or Password.')

    return render(request, 'login.html')


def bookdoctor(request,id):
    if request.method == "POST":
        name = request.POST.get('username')
        place = request.POST.get('place')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        print(date)
        print(type(date))
        data = Hospitalreg()
        data.Patient_name = name
        data.Age = age
        data.Place = place
        data.Phone = phone
        data.Date=date
        data.Doctor_id = DoctorModel.objects.get(Doctor_id=id)
        data.Token=Hospitalreg.objects.filter(Doctor_id=DoctorModel.objects.get(Doctor_id=id),Date=date).count()+1

        data.save()
        return redirect('/')
    return render(request, 'Bookdoctor.html')


def hospitalsign(request):
    if request.method == "POST":
        hospitalname = request.POST.get('hospital')
        booking = request.POST.get('book')
        license = request.POST.get('license')
        city = request.POST.get('city')
        password = request.POST.get('password')

        exists = HospitalModel.objects.filter(Hospital_Name=hospitalname).exists()
        if exists:
            messages.error(request, 'number already exits')
            return redirect('hospitalsignup')
        else:
            data = HospitalModel(Hospital_Name=hospitalname, Booking_no=booking, License_no=license, Password=password,
                                 City_id=CityModel.objects.get(City_Name=city))
            data.save()

    return render(request, 'Hospitalsign.html')


def hospitallogin(request):
    if request.method == 'POST':
        hospitalname = request.POST.get('hospital')
        password = request.POST.get('password')

        check_user = HospitalModel.objects.filter(Hospital_Name=hospitalname, Password=password)
        if check_user:

            request.session['mydata'] = hospitalname

            return redirect('/')
        else:
            return HttpResponse('Please enter valid Username or Password.')

    return render(request, 'Hospitallogin.html')


def doctorregi(request):
    if 'mydata' in request.session:
        print('aaaa')
        if request.method == 'POST':
            mydata = request.session['mydata']

            image = request.FILES.get('image')
            doctorname = request.POST.get('doctorname')
            department = request.POST.get('department')
            starttime = request.POST.get('starttime')
            endtime = request.POST.get('endtime')

            data = DoctorModel()
            data.Doctor_name = doctorname
            data.Department_name = department
            data.Start_time = starttime
            data.End_time = endtime
            data.images = image
            data.Hospital_id = HospitalModel.objects.get(Hospital_Name=mydata)
            data.save()
            return redirect('/')

    return render(request, 'RegisterDoctor.html')


# def category(request):
#     if request.method =="POST":
#         search=request.POST.get('category')
#         data=DonationCategoryModel.objects.filter(Category_id=DonationCategoryModel.objects.get(Category_Name=search))
#         return render(request,'Category.html',{'data':data})
#     return render(request,'Category.html')

def donation(request):
    return render(request, 'Donation.html')


def blooddonation(request):
    data = CityModel.objects.all()

    if 'user' in request.session:
        print('aaaa')


    if request.method == "POST":
        username = request.session['user']
        des = request.POST.get('des')
        contact = request.POST.get('contact')

        age = request.POST.get('age')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        bloodgroup = request.POST.get('bloodgroup')
        weight = request.POST.get('weight')
        disease = request.POST.get('disease')
        describe = request.POST.get('describe')
        proof = request.POST.get('proof')
        proofimage = request.FILES['proofimage']
        city = request.POST.get('city')
        data = BloodDonationModel()
        data.User_id = UserModel.objects.get(Username=username)
        data.City_id = CityModel.objects.get(City_id=city)
        data.Age = age
        data.Address = address
        data.Gender = gender
        data.Blood_group = bloodgroup
        data.Weight = weight
        data.Disease = disease
        data.Describe = describe
        data.Id_proof = proof
        data.Id_proofimage = proofimage
        data.BloodDonation_description = des
        data.Contact_Number = contact
        data.Category_id = DonationCategoryModel.objects.get(Category_Name='BLOOD DONATION')
        data.save()
        return render(request, 'BloodDonation.html')

    return render(request, 'BloodDonation.html',{'dataa': data})


def donar(request):
    if 'user' in request.session:
        print('aaaa')

    details = BloodDonationModel.objects.all()
    if request.method == "POST":
        search = request.POST.get('search')
        details = BloodDonationModel.objects.filter(
            Q(City_id__City_Name__icontains=search) | Q(Blood_group__icontains=search))

    return render(request, 'blooddonordetails.html', {'details': details})


def fooddonar(request):
    data = FoodModel.objects.all()
    if 'user' in request.session:
        print('aaaa')

    return render(request, 'FoodDonation.html', {'data': data})


def fooddonationreg(request,id):
    data = CityModel.objects.all()

    if 'user' in request.session:
        print('aaaa')


    if request.method == "POST":
        data=CityModel.objects.all()
        username = request.session['user']

        food = request.POST.get('fooditem')

        quantity = request.POST.get('quantity')
        contact = request.POST.get('contact')
        proof = request.POST.get('proof')
        proofimagee = request.FILES['idproof']
        city = request.POST.get('city')
        data = Fooddonationreg()
        data.User_id = UserModel.objects.get(Username=username)
        data.City_id = CityModel.objects.get(City_id=city)
        data.Food_item = food
        data.Food_Quantity = quantity
        data.Id_prooof = proof
        data.Id_proofimageee = proofimagee
        data.Contact_No = contact
        data. FoodDonation_id = FoodModel.objects.get(FoodDonation_id=id)
        data.save()
        return render(request, 'Registerfood.html')

    return render(request, 'Registerfood.html',{'dataa': data})


def profile(request):
    if 'user' in request.session:
        print(request.session["user"])
        username = request.session["user"]
        dataa = UserModel.objects.filter(Username=username)
        image = UserImageModel.objects.filter(User_id=UserModel.objects.get(Username=username)).first()

        print(dataa.values())

        return render(request, "profile.html", {'profile': dataa, 'image': image})
    else:
        return redirect('/login')

def editprofile(request):
    if 'user' in request.session:
        print(request.session["user"])
        username = request.session["user"]
        dataa = UserModel.objects.filter(Username=username)
        image = UserImageModel.objects.filter(User_id=UserModel.objects.get(Username=username)).first()


        print(dataa.values())

        return render(request, "editprofile.html", {'profile': dataa, 'image': image})
    return render(request,'editprofile.html')

def hospitalhom(request):
    return render(request,'Hospitalhome.html')

def viewdoctor(request):
    if 'mydata' in request.session:
        print(request.session["mydata"])
        username = request.session["mydata"]
        dataa = DoctorModel.objects.filter(Hospital_id=HospitalModel.objects.get(Hospital_Name=username))

    return render(request,"Doctorview.html")
