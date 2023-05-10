from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Bloodbank

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("name","mobile_number", "blood_group","address","vol_of_blood","date")



admin.site.register(Bloodbank, MemberAdmin)

