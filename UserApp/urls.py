from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('', views.Home, name="home"),
    path('driver', views.Driver, name="driver"),
    path('hospital',views.Hospital,name="hospital"),
    path('doctor/<int:id>',views.Doctor,name="doctor"),
    path('camp',views.Camp,name="camp"),
    path('campreg/<int:id>',views.campreg),
    path('campp/<int:id>',views.campregistration,name="campp"),
    path('sign/',views.sign,name="sign"),
    path('login/',views.login,name="login"),
    path('bookdoctor/<int:id>',views.bookdoctor,name="bookdoctor"),
     path('hospital_login',views.hospitallogin,name="hospitallogin"),
    path('hospital_sign', views.hospitalsign, name="hospitalsignup"),
     path('hospitalhome/',views.hospitalhom,name="hospitalhome"),
    # path('hosview',views.hospitalview),
    path('doctorregi',views.doctorregi,name="doctorregi"),
    path('blood/',views.blooddonation,name="blood"),
    path('donor',views.donar,name="donor"),
    path('fooddonor/',views.fooddonar,name="fooddonor"),
    path('foodreg/<int:id>',views.fooddonationreg,name="foodreg"),
    path('viewprofile',views.profile,name="viewprofile"),



]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
