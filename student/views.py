from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings    # 获取 settings.py 里边配置的信息
import os
from .models import *

# 1.1.前往 index 页（all）
def all_page(request):

    data = student_info.objects.all()
    content={'data': data}
    return render(request, 'student/all.html', content)

# 1.2.前往 add 页
def add_page( request ):
    return render(request, 'student/add.html')



# 2.增
@csrf_exempt
def add_student(request):
    t_name = request.POST['tName']
    t_age = request.POST['tAge']
    t_image = request.FILES['tImage']
    print(t_image.name)
    fname = os.path.join(settings.MEDIA_ROOT, t_image.name)  #上传的本地图片地址
    with open(fname, 'wb+') as pic:  #打开地址以二进制的写操作
        for chunk in t_image.chunks():  # 分块写入文件 可以将大文件按块写入到服务器中
            pic.write(chunk)
            # return HttpResponse("upload over!")

    student=student_info()
    student.t_name=t_name
    student.t_age=t_age
    # 存访问路径到数据库
    student.t_image = os.path.join("/static/media/", t_image.name)
    student.save()

    return redirect('/allPage')

# 3.1.查 - name-id
def search_student(request):
    if request.method=='GET':

        name_id=request.GET.get('name-id')
        if name_id:
            if type(name_id) ==str:
                student = student_info.objects.filter(t_name=name_id) or student_info.objects.filter(id=name_id)
                content = {'data': student}
                return render(request, 'student/all.html', content)
        else:
            return render(request, 'student/all.html')
# 4.1.前往 更改 页- id
def update_page(request,student_id):
    student=student_info.objects.filter(id=student_id)
    content = {'data': student}
    print(content)
    return  render(request,'student/update.html',content)
# 4.2 改
@csrf_exempt
def update_student(request):

    id=request.POST['t_id']
    t_name = request.POST['tName']
    t_age = request.POST['tAge']
    # 缺陷：文件必传
    t_image = request.FILES['tImage']

    fname = os.path.join(settings.MEDIA_ROOT, t_image.name)
    with open(fname, 'wb') as pic:
        for chunk in t_image.chunks():
            pic.write(chunk)
    t_image = os.path.join("/static/media/", t_image.name) #更改后的图片地址

    student_info.objects.filter(id=id).update(t_name=t_name,t_age=t_age,t_image=t_image)
    return redirect('/allPage')

# 5.删
def delete_student(request,student_id):
    student_info.objects.filter(id=student_id).delete()
    return redirect('/allPage')
