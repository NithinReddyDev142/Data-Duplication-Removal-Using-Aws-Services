from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from userapp.models import *
from mainapp.models import *
from cloudapp.models import *
from django.db.models import Q

# Create your views here.

# cloud login

def cloud_login(request):
    if request.method=='POST':
        cloud=request.POST.get('cloud')
        cloud=request.POST.get('cloud')
        if cloud=='cloud' and cloud=='cloud':
            return redirect('cloud_dashboard')
    return render(request,'user/cloud-login.html')


def cloud_dashboard(request):
    users=userModel.objects.count()
    file=file_uploadModel.objects.count()
    return render(request,'cloud/cloud-dashboard.html',{'users':users,'file':file})


def cloud_manage_users(request):
    data=userModel.objects.all().order_by("reg_date")

    if request.method=='POST':
         search=request.POST.get('search')
         data=userModel.objects.filter(Q(user_id__icontains=search) | Q(user_name__icontains=search)  | Q(email__icontains=search) | Q(mobile__icontains=search) | Q(location__icontains=search) | Q(reg_date__icontains=search))

    return render(request,'cloud/cloud-manage-users.html',{'data':data})


def cloud_view_files(request):
    data=file_uploadModel.objects.all().order_by("file_uploded_date")
    if request.method=="POST" :
     search=request.POST.get('search')
     data=file_uploadModel.objects.filter(Q(file_id__icontains=search) | Q(file_name__icontains=search)  | Q(file__icontains=search) | Q(file_type__icontains=search) | Q(file_size__icontains=search) | Q(file_uploded_date__icontains=search))
    return render(request,'cloud/cloud-view-files.html',{'data':data})


def cloud_user_authentications(request):
    data=file_uploadModel.objects.all().order_by("file_uploded_date")
    if request.method=="POST" :
     search=request.POST.get('search')
     data=file_uploadModel.objects.filter(Q(file_id__icontains=search) | Q(file_name__icontains=search)  | Q(file__icontains=search) | Q(file_type__icontains=search) | Q(file_size__icontains=search) | Q(file_uploded_date__icontains=search))
    return render(request,'cloud/cloud-user-authentications.html',{'data':data})    

def accept_user(request,id):
    accept=get_object_or_404(userModel,user_id=id)
    accept.status='Accepted'
    accept.save(update_fields=['status'])
    accept.save()
    return redirect('cloud_manage_users')

def reject_user(request,id):
    accept=get_object_or_404(userModel,user_id=id)
    accept.status='Rejected'
    accept.save(update_fields=['status'])
    accept.save()
    return redirect('cloud_manage_users') 


def accept_file(request,id):
    accept=get_object_or_404(file_uploadModel,file_id=id)
    accept.status='Accepted'
    accept.save(update_fields=['status'])
    accept.save()
    return redirect('cloud_user_authentications')

def reject_file(request,id):
    accept=get_object_or_404(file_uploadModel,file_id=id)
    accept.status='Rejected'
    accept.save(update_fields=['status'])
    accept.save()
    return redirect('cloud_user_authentications')      


