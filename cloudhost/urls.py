"""cloudhost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ast import If
from xml.dom.minidom import Document


from django.conf.urls.static import static
from django.conf import settings
from cloudapp import views as cloudapp_views
from userapp import views as userapp_views
from mainapp import views as mainapp_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',mainapp_views.home,name='home'),





# cloud


    path('cloud_login',cloudapp_views.cloud_login,name='cloud_login'),

    path('cloud_dashboard', cloudapp_views.cloud_dashboard,name='cloud_dashboard'),

    path('cloud_manage_users', cloudapp_views.cloud_manage_users,name='cloud_manage_users'),

    path('cloud_view_files', cloudapp_views.cloud_view_files,name='cloud_view_files'), 
    
    path('cloud_user_authentications',cloudapp_views.cloud_user_authentications,name='cloud_user_authentications'),

    path('accept_file/<int:id>/',cloudapp_views.accept_file,name='accept_file'),

    path('reject_file/<int:id>/',cloudapp_views.reject_file,name='reject_file'),
    
    path('accept_user/<int:id>/',cloudapp_views.accept_user,name='accept_user'),

    path('reject_user/<int:id>/',cloudapp_views.reject_user,name='reject_user'),
    

# main
    
    # path('home', mainapp_views.home,name='home'),


# user
    path('user_otp',userapp_views.user_otp,name='user_otp'),

    path('user_login',userapp_views.user_login,name='user_login'),

    path('user_register', userapp_views.user_register,name='user_register'),

    path('user_dashboard', userapp_views.user_dashboard,name='user_dashboard'),

    
    path('download_btn/<int:id>/', userapp_views.download_btn,name='download_btn'), 

    path('download_file',userapp_views.download_file,name='download_file'),

    path('download_otp',userapp_views.download_otp,name='download_otp'),

    path('data_search', userapp_views.data_search,name='data_search'), 
    
    path('data_storage',userapp_views.data_storage,name='data_storage'),

    path('data_download', userapp_views.data_download,name='data_download'), 

    path('key_verification', userapp_views.key_verification,name='key_verification'), 
    
    path('profile',userapp_views.profile,name='profile'),



]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)