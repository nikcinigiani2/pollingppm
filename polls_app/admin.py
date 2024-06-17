from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .Models import Poll, Choice

admin.site.register(Poll)
admin.site.register(Choice)