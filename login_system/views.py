
from ast import Pass
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.cache import cache_control
from .models import Users
# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        print(username)
        print(password)
    print("index")
    return render(request,'index.html')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def reg(request):
    print("home")
    if request.method == 'POST':
        
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        passw = request.POST.get('pass1')
        address =request.POST.get('address')
        city = request.POST.get('city')
        staten = request.POST.get('state')
        zip = request.POST.get('zip')

        print("fname-"+fname)
        print("lname-"+lname)
        print("email-"+email)
        print(phone)
        print("pass-"+str(passw))
        print("address-"+address)
        print("city-"+city)
        print("state-"+str(staten))
        print("zip-"+str(zip))


        # return render(request,'home.html')

    return render(request,'home.html')
def home(request):
    user_details = Users.objects.all()
    return render(request,'home.html',{'u_details':user_details})



def logout(request):
    return Pass