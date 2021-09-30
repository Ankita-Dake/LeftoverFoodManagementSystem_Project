from django.contrib import messages, auth
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import AgentRegistration
from .forms import DonorRegistration
from .forms import DonateForm
from .forms import DonorForm
from .models import Agent
from .models import Donor
from .models import Donate
from .models import Donorform
import requests
import smtplib as s


def send_email(email):
    ob = s.SMTP("smtp.gmail.com", 587)
    ob.starttls()
    ob.login("ankitadake1997@gmail.com", 'anku@1993')
    subject = "Sending email for Food Waste"
    body = "Accept Request for Food"
    message = "subject:{}\n\n{}".format(subject, body)
    print(message)

    ob.sendmail(email,"ankitadake1997@gmail.com", message)
    print("send successfully")
    ob.quit()


# Create your views here.
def home(request):
    context = {}
    return render(request, 'food/home.html', context)


def aboutus(request):
    context = {}
    return render(request, 'food/aboutus.html', context)


def ourmission(request):
    context = {}
    return render(request, 'food/ourmission.html', context)


def contactus(request):
    context = {}
    return render(request, 'food/contactus.html', context)


def LoginRegister(request):
    context = {}
    return render(request, 'food/LoginRegister.html', context)


def adminlogin(request):
    if request.method == "POST":
        ar = AuthenticationForm(request=request, data=request.POST)
        if ar.is_valid():
            us = ar.cleaned_data['username']
            pw = ar.cleaned_data['password']
            user = authenticate(username=us, password=pw)
            if user is not None:
                auth.login(request, user)
        return HttpResponseRedirect('/AdminView/')
    else:
        ar = AuthenticationForm()
    return render(request, 'food/adminlogin.html', {'form': ar})


def logout(request):
    auth.logout(request)
    return redirect('/')


def Agent_Login(request):
    if request.method == "POST":
        ar = AuthenticationForm(request=request, data=request.POST)
        if ar.is_valid():
            us = ar.cleaned_data['username']
            pw = ar.cleaned_data['password']
            user = authenticate(username=us, password=pw)
            if user is not None:
                auth.login(request, user)
        return HttpResponseRedirect('/AgentMainProfile/')
    else:
        ar = AuthenticationForm()
    return render(request, 'food/AgentLogin.html', {'form': ar})


def Donor_Login(request):
    if request.method == "POST":
        dr = AuthenticationForm(request=request, data=request.POST)
        if dr.is_valid():
            us = dr.cleaned_data['username']
            pw = dr.cleaned_data['password']
            user = authenticate(username=us, password=pw)
            if user is not None:
                login(request, user)
        return HttpResponseRedirect('/DonorMainProfile/')
    else:
        dr = AuthenticationForm()
    return render(request, 'food/DonorLogin.html', {'form': dr})


def AgentMainProfile(request):
    context = {}
    return render(request, 'food/AgentMainProfile.html', context)


def DonorMainProfile(request):
    context = {}
    return render(request, 'food/DonorMainProfile.html', context)


def agentprofile(request):
    agentpro = Agent.objects.all()
    return render(request, 'food/agentprofile.html', {'agentprofile': agentpro})


def donordetails(request):
    donorpro = Donor.objects.all()
    return render(request, 'food/donordetails.html', {'donordetails': donorpro})


def AdminView(request):
    adminpro = Donorform.objects.all()
    adminpro1 = Agent.objects.all()
    return render(request, 'food/AdminView.html', {'AdminView': adminpro, 'agentprofile': adminpro1})


def MyDonationsRecords(request):
    Donatepro = Donate.objects.all()
    return render(request, 'food/MyDonationsRecords.html', {'MyDonationsRecords': Donatepro})


def showformdata(request):
    if request.method == 'POST':
        ar = AgentRegistration(request.POST)
        if ar.is_valid():
            nm = ar.cleaned_data['name']
            em = ar.cleaned_data['email']
            us = ar.cleaned_data['username']
            pw = ar.cleaned_data['password']
            contact = ar.cleaned_data['contact']
            add = ar.cleaned_data['address']
            city = ar.cleaned_data['city']
            reg = Agent(name=nm, email=em, username=us, password=pw, contact=contact, address=add, city=city)
            reg.save()
            send_sms(contact, "Signup successfully")
            return redirect('/AgentLogin')
    else:
        ar = AgentRegistration()
    return render(request, 'food/agent.html', {'form': ar})


def send_sms(contact, message):
    url = 'https://www.fast2sms.com/dev/bulkV2'
    params = {
        'authorization': '6TupmcoOeQjBzGWVawnM2v9KhU7iH43l1brIYdtAysNJ0F8Ef5rwvHhSJcsKZWlmnNFRA3C89PYVXigG',
        'sender_id': 'TXTIND',
        'message': message,
        'language': 'english',
        'route': 'v3',
        'numbers': contact

    }
    response = requests.get(url, params=params)
    dict = response.json()
    print(dict)


def donorformdata(request):
    if request.method == 'POST':
        dr = DonorRegistration(request.POST)
        if dr.is_valid():
            nm = dr.cleaned_data['name']
            em = dr.cleaned_data['email']
            us = dr.cleaned_data['username']
            pw = dr.cleaned_data['password']
            contact = dr.cleaned_data['contact']
            resname = dr.cleaned_data['restaurantname']
            resadd = dr.cleaned_data['restaurantaddress']
            city = dr.cleaned_data['city']
            reg = Donor(name=nm, email=em, username=us, password=pw, contact=contact, restaurantname=resname,
                        restaurantaddress=resadd, city=city)
            reg.save()
            return redirect('/DonorLogin')
    else:
        dr = DonorRegistration()
    return render(request, 'food/donor.html', {'form': dr})


def agentdonateform(request):
    if request.method == 'POST':
        df = DonateForm(request.POST)
        if df.is_valid():
            nm = df.cleaned_data['Agent_name']
            em = df.cleaned_data['email']
            dn = df.cleaned_data['Donor_name']
            docf = df.cleaned_data['DateOfCollectingFood']
            tocf = df.cleaned_data['TimeOfCollectingFood']
            quan = df.cleaned_data['Quantity']
            orn = df.cleaned_data['Orphanage_name']
            city = df.cleaned_data['city']
            reg = Donate(Agent_name=nm, email=em, Donor_name=dn, DateOfCollectingFood=docf, TimeOfCollectingFood=tocf,
                         Quantity=quan,
                         Orphanage_name=orn, city=city)
            reg.save()
            return redirect('/AgentMainProfile')
    else:
        df = DonateForm()
    return render(request, 'food/AgentDonateForm.html', {'form': df})


def donordonateform(request):
    if request.method == 'POST':
        Df = DonorForm(request.POST)
        if Df.is_valid():
            dn = Df.cleaned_data['Donor_name']
            em = Df.cleaned_data['email']
            contact = Df.cleaned_data['contact']
            da = Df.cleaned_data['Donor_address']
            rn = Df.cleaned_data['restaurant_name']
            rd = Df.cleaned_data['restaurant_address']
            tof = Df.cleaned_data['TypeOfFood']
            doc = Df.cleaned_data['DateOfCooking']
            quan = Df.cleaned_data['Quantity']
            city = Df.cleaned_data['city']
            reg1 = Donorform(Donor_name=dn, email=em, contact=contact, Donor_address=da, restaurant_name=rn,
                             restaurant_address=rd, TypeOfFood=tof, DateOfCooking=doc, Quantity=quan, city=city)
            reg1.save()
            send_email(em)
            messages.add_message(request, messages.SUCCESS, 'your Message sent to admin')
            return redirect('/DonorMainProfile')
    else:
        Df = DonorForm()
    return render(request, 'food/DonateNow.html', {'form': Df})
