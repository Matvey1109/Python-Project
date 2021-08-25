from django.contrib import admin
from .models import Contact, ContactPermissions

admin.site.register(Contact)
admin.site.register(ContactPermissions)
