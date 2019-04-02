from django.contrib import admin

# Register your models here.
#往数据库注册表单
from .models import student_info

admin.site.register(student_info)
