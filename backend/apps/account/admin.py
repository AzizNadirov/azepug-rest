from django.contrib import admin
from .models import Contacts, Profile

admin.site.register(Profile)
admin.site.register(Contacts)