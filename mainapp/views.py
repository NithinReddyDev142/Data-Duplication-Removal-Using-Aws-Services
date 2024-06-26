from django.shortcuts import render
from django.shortcuts import render

from userapp.models import *
from django.contrib import messages
from django.db.models import Q
# Create your views here.




def home(request):
    return render(request,'main/index.html')

