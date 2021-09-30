from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('agent/', views.showformdata, name="agent"),
    path('AgentMainProfile/',views.AgentMainProfile,name="AgentMainProfile"),
    path('DonorMainProfile/',views.DonorMainProfile,name="DonorMainProfile"),
    path('donor/', views.donorformdata, name="donor"),
    path('agentprofile/', views.agentprofile, name="agentprofile"),
    path("MyDonationsRecords/",views.MyDonationsRecords,name ='MyDonationsRecords'),
    path('donordetails/', views.donordetails, name="donordetails"),
    path('LoginRegister/', views.LoginRegister, name="LoginRegister"),
    path('AgentLogin/', views.Agent_Login, name="AgentLogin"),
    path('DonorLogin/', views.Donor_Login, name="DonorLogin"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('AgentDonateForm/',views.agentdonateform,name="AgentDonateForm"),
    path('DonateNow/',views.donordonateform,name="DonateNow"),
    path('AdminView/',views.AdminView,name="AdminView"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('ourmission/',views.ourmission,name="ourmission"),
    path('contactus/',views.contactus,name="contactus"),
    path('logout/',views.logout,name="logout")
]
