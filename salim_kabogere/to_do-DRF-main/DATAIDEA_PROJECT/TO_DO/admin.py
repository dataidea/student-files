from django.contrib import admin
from .models import MemberLogin, MemberRegistration, ToDo

# Register your models here.
admin.site.register(MemberRegistration)
admin.site.register(MemberLogin)
admin.site.register(ToDo)