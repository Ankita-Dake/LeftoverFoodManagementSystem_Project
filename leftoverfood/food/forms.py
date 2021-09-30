from django import forms
# from django.contrib.auth.models import Agent
from .models import Agent
from django.forms import TextInput, EmailInput


class AgentRegistration(forms.Form):
    name = forms.CharField(error_messages={'required': 'enter your name'},widget=forms.TextInput(
        attrs={'placeholder': 'Name', 'style': 'width:300px;', 'class': 'form-control'}))
    email = forms.EmailField(error_messages={'required': 'enter your email'}, min_length=5, max_length=50,widget=forms.EmailInput(
        attrs={'placeholder': 'Email', 'style': 'width:300px;', 'class': 'form-control'}))
    username = forms.CharField(error_messages={'required ': 'enter your username'}, min_length=5, max_length=20,widget=forms.TextInput(
        attrs={'placeholder': 'Name', 'style': 'width:300px;', 'class': 'form-control'}))
    password = forms.CharField(error_messages={'required': 'enter your email'},
                               min_length=5, max_length=50,widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'style': 'width:300px;', 'class': 'form-control'}))
    contact = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'Contact', 'style': 'width:300px;', 'class': 'form-control'}))
    address = forms.CharField(error_messages={'required': 'enter your address'},widget=forms.TextInput(
        attrs={'placeholder': 'Address', 'style': 'width:300px;', 'class': 'form-control'}))
    city = forms.CharField(error_messages={'required': 'enter your city'},widget=forms.TextInput(
        attrs={'placeholder': 'city', 'style': 'width:300px;', 'class': 'form-control'}))


# def clean(self):
#     cleaned_data = super().clean()
#     valname = self.cleaned_data['name']
#     valemail = self.cleaned_data['email']
#     valpassword = self.cleaned_data['password']
#     valaddress = self.cleaned_data['address']
#     valcity = self.cleaned_data['city']
# if len(valname) < 4:
#     raise forms.validationError('Name should be more than 4')
# if len(valemail) <15 :
#     raise forms.validationError('email should be more than 15')
# if len(valpassword) <5:
#     raise forms.validationError('password should be more than  5')
# if len(valaddress) < 10:
#     raise forms.validationError('Name should be more than 10')

class DonorRegistration(forms.Form):
    name = forms.CharField(error_messages={'required': 'enter your name'}, widget=forms.TextInput(
        attrs={'placeholder': 'Name', 'style': 'width:300px;', 'class': 'form-control'}))
    email = forms.EmailField(error_messages={'required': 'enter your email'}, min_length=5, max_length=50,
                             widget=forms.EmailInput(
                                 attrs={'placeholder': 'Name', 'style': 'width:300px;', 'class': 'form-control'}))
    username = forms.CharField(error_messages={'required ': 'enter your username'}, min_length=5, max_length=20,
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'Name', 'style': 'width:300px;', 'class': 'form-control'}))
    password = forms.CharField(error_messages={'required': 'enter your email'},
                               min_length=5, max_length=50,widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'style': 'width:300px;', 'class': 'form-control'}))
    contact = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'Contact', 'style': 'width:300px;', 'class': 'form-control'}))
    restaurantname = forms.CharField(error_messages={'required': 'enter your  restaurant name'}, widget=forms.TextInput(
        attrs={'placeholder': 'Name', 'style': 'width:300px;', 'class': 'form-control'}))
    restaurantaddress = forms.CharField(error_messages={'required': 'enter your address'}, widget=forms.TextInput(
        attrs={'placeholder': 'Address', 'style': 'width:300px;', 'class': 'form-control'}))
    city = forms.CharField(error_messages={'required': 'enter your city'}, widget=forms.TextInput(
        attrs={'placeholder': 'city', 'style': 'width:300px;', 'class': 'form-control'}))


class DonateForm(forms.Form):
    Agent_name = forms.CharField(error_messages={'required': 'enter your name'},
                                 widget=forms.TextInput(
                                     attrs={'placeholder': 'Name', 'style': 'width:300px;', 'class': 'form-control'}))
    email = forms.EmailField(error_messages={'required': 'enter your email'}, min_length=5, max_length=50,
                             widget=forms.EmailInput(
                                 attrs={'placeholder': 'Email', 'style': 'width:300px; ',
                                        'class': 'form-control'}))
    Donor_name = forms.CharField(error_messages={'required ': 'enter your name'}, min_length=5, max_length=20,
                                 widget=forms.TextInput(
                                     attrs={'placeholder': 'Donor Name', 'style': 'width:300px;',
                                            'class': 'form-control'}))
    DateOfCollectingFood = forms.DateField(widget=forms.DateInput(
        attrs={'placeholder': 'Date', 'style': 'width:300px;', 'class': 'form-control'}))
    TimeOfCollectingFood = forms.TimeField(widget=forms.TimeInput(
        attrs={'placeholder': 'Time', 'style': 'width:300px; ', 'class': 'form-control'}))
    Quantity = forms.IntegerField(widget=forms.TextInput(
        attrs={'placeholder': 'Name', 'style': 'width:300px; ', 'class': 'form-control'}))
    Orphanage_name = forms.CharField(error_messages={'required': 'enter your name'}, widget=forms.TextInput(
        attrs={'placeholder': 'Name', 'style': 'width:300px; ', 'class': 'form-control'}))
    city = forms.CharField(error_messages={'required': 'enter your name'}, widget=forms.TextInput(
        attrs={'placeholder': 'Name', 'style': 'width:300px; ', 'class': 'form-control'}))


class DonorForm(forms.Form):
    Donor_name = forms.CharField(error_messages={'required': 'enter your name'}, widget=forms.TextInput(
        attrs={'placeholder': 'Name', 'style': 'width:300px; ', 'class': 'form-control'}))
    email = forms.EmailField(error_messages={'required': 'enter your email'}, min_length=5, max_length=50,
                             widget=forms.EmailInput(
                                 attrs={'placeholder': 'Name', 'style': 'width:300px; ', 'class': 'form-control'}))
    contact = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'Contact', 'style': 'width:300px; ', 'class': 'form-control'}))
    Donor_address = forms.CharField(error_messages={'required ': 'enter your address'}, min_length=5, max_length=20,
                                    widget=forms.TextInput(
                                        attrs={'placeholder': 'Address', 'style': 'width:300px;',
                                               'class': 'form-control'}))
    restaurant_name = forms.CharField(error_messages={'required ': 'enter your name '}, min_length=5, max_length=20,
                                      widget=forms.TextInput(
                                          attrs={'placeholder': 'Name', 'style': 'width:300px; ',
                                                 'class': 'form-control'}))
    restaurant_address = forms.CharField(error_messages={'required ': 'enter your address'}, min_length=5,
                                         max_length=20, widget=forms.TextInput(
            attrs={'placeholder': 'Address', 'style': 'width:300px; ', 'class': 'form-control'}))
    TypeOfFood = forms.CharField(error_messages={'required': 'enter your type'}, widget=forms.TextInput(
        attrs={'placeholder': 'Type Of Food', 'style': 'width:300px; ', 'class': 'form-control'}))
    DateOfCooking = forms.DateField(widget=forms.DateInput(
        attrs={'placeholder': 'Date', 'style': 'width:300px; ', 'class': 'form-control'}))
    Quantity = forms.CharField(error_messages={'required': 'enter your quantity'}, widget=forms.NumberInput(
        attrs={'placeholder': 'Quantity', 'style': 'width:300px; ', 'class': 'form-control'}))
    city = forms.CharField(error_messages={'required': 'enter your city'}, widget=forms.TextInput(
        attrs={'placeholder': 'city', 'style': 'width:300px; ', 'class': 'form-control'}))
