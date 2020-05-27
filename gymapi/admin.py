from django.contrib import admin

# Register your models here.

from .models import customer,User

admin.site.register(customer)
admin.site.register(User)

