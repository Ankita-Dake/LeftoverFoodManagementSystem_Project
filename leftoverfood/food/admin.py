from django.contrib import admin

from .models import Agent
from .models import Donor
from .models import Donate
from .models import Donorform


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'username', 'password', 'contact', 'address', 'city')


@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'username', 'password', 'contact', 'restaurantname', 'restaurantaddress', 'city')


@admin.register(Donate)
class DonateAdmin(admin.ModelAdmin):
    list_display = (
        'Agent_name', 'email', 'Donor_name', 'DateOfCollectingFood', 'TimeOfCollectingFood', 'Quantity',
        'Orphanage_name',
        'city')


@admin.register(Donorform)
class DonateNowAdmin(admin.ModelAdmin):
    list_display = (
        'Donor_name', 'email','contact', 'Donor_address', 'restaurant_name', 'restaurant_address', 'TypeOfFood',
        'DateOfCooking', 'Quantity', 'city')
