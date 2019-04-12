from django.contrib import admin

# Register your models here.
from .models import Academic_dept, Academic_class, Upload

admin.site.register(Academic_dept)
admin.site.register(Academic_class)
admin.site.register(Upload)
