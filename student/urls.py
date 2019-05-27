#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: taojian
@file: urls.py
@time: 2019/5/20 18:46
@software: PyCharm
"""


from django.conf.urls import url

from student import views
app_name='login'
urlpatterns = [
    url(r'^allPage/$', views.all_page),   # 前往所有学生的网页

    # 注意大小写哦
    url(r'^addPage/$', views.add_page),     # 前往新增学生的网页
    url(r'^addStudent/$', views.add_student),   # 添加学生的 dao 操作
    url(r'^search/$', views.search_student),   # 根据 t_name 查找学生的 dao 操作
    url(r'^get/(?P<student_id>[0-9]*)/$', views.update_page),  # 根据 id 查找学生的 dao 操作
    url(r'^updateStudent/$', views.update_student),   # 修改学生的 dao 操作
    url(r'^delete/(?P<student_id>[0-9]*)/$', views.delete_student),   # 删除学生的 dao 操作


]