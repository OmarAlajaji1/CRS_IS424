from django.contrib import admin
from .models import *


class collegeadmin(admin.ModelAdmin):
    list_display=("collegeid","name")

class ccourseadmin(admin.ModelAdmin):
    list_display=("name","courseid","hours","hostcollege","instructor","dicription")


class studentadmin(admin.ModelAdmin):
    list_display=()

# Register your models here.
admin.site.register(College,collegeadmin)
admin.site.register(Student,studentadmin)
admin.site.register(Course,ccourseadmin)







