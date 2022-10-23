from django.contrib import admin

# Register your models here.
from .models import BasicInfo, Survey

admin.site.register(BasicInfo)
admin.site.register(Survey)