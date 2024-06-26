from re import M
from django.shortcuts import render
from ast import Pass
from dataclasses import field
from tkinter.tix import COLUMN
from urllib import request
from email.headerregistry import Address
from unicodedata import name
from django.contrib import messages
from tabnanny import check
from django.shortcuts import render
from userapp.models import *
from django.shortcuts import render,redirect,get_object_or_404
from userapp.views import *
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.db.models import Q
import random
import requests
# Create your views here.


#user login
def user_login(request):
     if request.method=='POST':
         email=request.POST.get('email')
         password=request.POST.get('password')

         try:     
            
            check=userModel.objects.get(email=email,password=password)
            request.session["user_id"]=check.user_id
            return redirect ('user_dashboard')
           
         except: 
             pass
     return render(request,'user/user-login.html')         


#user register
def user_register(request):
    if request.method=='POST' and request.FILES['user_image']:
        user_name=request.POST ['user_name'] 
        email=request.POST['email']       
        password=request.POST['password']
        mobile=request.POST['mobile']
        dob=request.POST['dob']
        location=request.POST['location']
        user_image=request.FILES['user_image']


        if userModel.objects.filter(email=email):
            messages.error(request,"Email ALready Exists!")

        else:
            otp=random.randint(1111,9999)
            url = "https://www.fast2sms.com/dev/bulkV2"
            # create a dictionary
            my_data = {'sender_id': 'FSTSMS', 
                        'message': 'Welcome to CloudHost, your verification OPT is '+str(otp)+ 'Thanks for request of OTP.', 
                        'language': 'english', 
                        'route': 'p', 
                        'numbers': mobile
            }

            # create a dictionary
            headers = {
                'authorization': '5S3Emx7a0GBgzHyjMNcYhUT6quoKPrZDkF82s9X4JA1IdWptVwMmITBzgKOpvWw0UiFeJLxbarREPS61',
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache"
            }
            # make a post request
            response = requests.request("POST",
                                        url,
                                        data = my_data,
                                        headers = headers)
            # print the send message
            print(response.text)        


        userModel.objects.create(user_name=user_name,password=password,mobile=mobile,email=email,dob=dob,location=location,user_image=user_image,otp=otp)
        messages.success(request,'Account Created Successfully!')
        return redirect('user_otp')
         
    return render(request,'user/user-register.html')



def user_otp(request):
    # user_id=request.session['user_id']

    if request.method == "POST":
        otp = request.POST.get('otp')
        print(otp)
        try:
            print('ppppppppppppppppppppp')
            check = userModel.objects.get(otp=otp)
            user_id = request.session['user_id']=check.user_id
            otp=check.otp
            print(otp)
            if otp == otp:
                userModel.objects.filter(user_id=user_id).update()
                messages.info(request,'')
                return redirect('user_dashboard')
            else:
                return redirect('user_otp')
        except:
            pass
    return render(request,'user/user-otp.html')


def user_dashboard(request):
    users=userModel.objects.count()
    file=file_uploadModel.objects.count()
    return render(request,'user/user-dashboard.html',{'users':users,'file':file})


def download_file(request):
    print("aaaaaaaaa")
    # print(id)
    print("bbbbbbbbbb")
    filedetails = file_uploadModel.objects.get(file_id=request.session["file_id"])
    file_id=filedetails.file_id 
    file_name = filedetails.file_name
    file=filedetails.file
    file_size = filedetails.file_size
    file_type=filedetails.file_type
    file=filedetails.file
    file_uploded_date=filedetails.file_uploded_date

    print(file) 

    return render(request,'user/download-file.html',{'file_id':file_id,'file':file,'file_type':file_type,'file_name':file_name,'file_size':file_size,'file_uploded_date':file_uploded_date})

def download_otp(request):
     if request.method == "POST":
        print("ggggggggggggggggggggggggggggggggggg")
        otp = request.POST.get('otp')
        print(otp)
        try:
            print('ppppppppppppppppppppp')
            check = file_uploadModel.objects.get(otp=otp)
            user_id = request.session['user_id']=check.user_id
            print("dddddddddddd")
            otp=check.otp
            print("ccccccccccccc")
            print(otp)
            if otp == otp:
                print("eeeeeeeeeee")
                userModel.objects.filter(user_id=user_id).update()
                messages.info(request,'')
                return redirect('download_file')
            else:
                return redirect('download_otp')
        except:
            pass


     if request.method == "POST":
        otp = request.POST.get('otp')
        print(otp)
        try:
            print('ppppppppppppppppppppp')
            check = userModel.objects.get(otp=otp)
            user_id = request.session['user_id']=check.user_id
            otp=check.otp
            print(otp)
            if otp == otp:
                userModel.objects.filter(user_id=user_id).update()
                messages.info(request,'')
                return redirect('user_dashboard')
            else:
                return redirect('user_otp')
        except:
            pass
     return render(request,'user/download-otp.html')



def data_search(request):
    data=file_uploadModel.objects.all().order_by("file_uploded_date")
    if request.method=="POST" :
     search=request.POST.get('search')
     data=file_uploadModel.objects.filter(Q(file_id__icontains=search) | Q(file_name__icontains=search)  |  Q(file_type__icontains=search) | Q(file_size__icontains=search) | Q(file_uploded_date__icontains=search))
    return render(request,'user/data-search.html',{'data':data})
    
def download_btn(request,id):
    request.session["file_id"] = id
    global otp1
    if request.method=="GET":
        cid = request.session["user_id"]
        data = userModel.objects.get(user_id=cid)
        u = data.mobile
        print(u)
        # obj = get_object_or_404(file_uploadModel,file_id=id)
        otp1=random.randint(111111,999999)
        # obj.otp=otp
        # obj.save(update_fields=['otp'])
        # obj.save()
        file_uploadModel.objects.filter(file_id=id).update(otp=otp1)
        file_id=file_uploadModel.objects.get(file_id=id)
        result=file_id.file_id

        url = "https://www.fast2sms.com/dev/bulkV2"
                # create a dictionary
        my_data = {'sender_id': 'FSTSMS', 
                            'message': 'Welcome to CloudHost, your Private Key is '+str(otp1)+ 'Thanks for request of OTP.', 
                            'language': 'english', 
                            'route': 'p', 
                            'numbers': u,
                                
                }

                # create a dictionary
        headers = {
                    'authorization': '5S3Emx7a0GBgzHyjMNcYhUT6quoKPrZDkF82s9X4JA1IdWptVwMmITBzgKOpvWw0UiFeJLxbarREPS61',
                    'Content-Type': "application/x-www-form-urlencoded",
                    'Cache-Control': "no-cache"
                }
                # make a post request
        response = requests.request("POST",
                                            url,
                                            data = my_data,
                                            headers = headers)
                # print the send message
        print(response.text) 

    if request.method=="POST":        
        # print('generated otp',otp1)
        entered_otp = int(request.POST.get('otp'))
        print('entered otp',entered_otp)
        
        if otp1 == entered_otp:
            return redirect('download_file')
            # return redirect('download_file', id=id)
            print('correct')
        else:
            return HttpResponseRedirect(request.path_info)

    return render(request,'user/download-otp.html',{'mobile':u,'file_id':result})
    

def data_storage(request):
    user_id=request.session['user_id']
    
    if request.method=='POST' and 'file' in request.FILES:
        file = request.FILES['file']
        file_name=file.name
        file_size=file.size
        file_type=file.content_type
        user_id=request.session["user_id"]
     

        try:
            if file_uploadModel.objects.filter(file_name=file_name).exists():
                messages.error(request,"Data Duplication").py
        
            else:
                data_storage=file_uploadModel.objects.create(file=file,file_name=file_name,file_size=file_size,file_type=file_type,user_id=user_id)
                data_storage.save()
                messages.info(request,"Uploaded Successfully")
                print('ggggggggggggggggggggggggggggggggggggggggggg')
        except:
            messages.error(request,"Upload failed..")
            
    print(messages)
    return render(request,'user/data-storage.html')


def data_download(request,):
   
    return render(request,'user/secure-data-download.html')    


def key_verification(request):
    return render(request,'user/key-verification.html')


def profile(request):
    user_id=request.session["user_id"]
    data = userModel.objects.get(user_id=user_id)
    obj = get_object_or_404(userModel,user_id=user_id)
    if request.method=='POST':
        print('ftttyy')
        user_name=request.POST['user_name']
        print(user_name)
        email=request.POST['email']
        mobile=request.POST['mobile']
        location=request.POST['location']
        dob = request.POST['dob']
        print('ddddddddddddddddddddd')
        if len(request.FILES) != 0:
            print("ggggggggggggggggggggggggggggggg")
            user_image = request.FILES['user_image']
            obj.user_name = user_name
            obj.mobile = mobile
            obj.email = email
            obj.location =location
            obj.dob = dob
            obj.user_image = user_image
            obj.save(update_fields=['user_name','mobile','email','location','user_image','dob'])
            obj.save()

   
        else:
            obj.user_name = user_name
            obj.mobile = mobile
            obj.email = email
            obj.location =location
            obj.dob = dob
            obj.save(update_fields=['user_name','mobile','email','location','dob'])
            obj.save()
       

          
  

   
    return render(request,'user/my-profile.html',{'data': data})