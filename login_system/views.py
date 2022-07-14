
from ast import Pass
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.cache import cache_control
from .models import Users
import sys
# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        print(username)
        print(password)
        # Raw Query
        user_log=Users.objects.raw('SELECT login_system_users.uid,login_system_users.first_name,login_system_users.passw FROM login_system_users')
        print("size of raw query variable is", end='')
        print(sys.getsizeof(user_log))
        print(user_log)
        for i in user_log:
            print(i.uid,end='-')
            print(i.first_name,end='-')
            print(i.passw)
            if username==i.first_name and password==i.passw:
                print(i.first_name)
                print("successs")
                #create session

                return JsonResponse(
                    {
                    'success':True},

                    safe=False
                
                )
        else :
            print("Failed")
            return JsonResponse(
                {
                'success':False},

                 safe=False
                
                )
         
            
        # print(user_log)
        # user_log=Users.objects.filter(first_name__contains=username)
        # print(type(user_log))
    print("index")
    return render(request,'index.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def reg(request):
    print("reg")
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
        user_tabel=Users(first_name=fname,last_name=lname,email=email,phone=phone,passw=passw,address=address,city=city,state=staten,zip=zip)
        user_tabel.save()
        return redirect(index)

    return render(request,'reg.html')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    print("home")
    user_details = Users.objects.all()
    return render(request,'home.html',{'u_details':user_details})



def logout(request):
    return Pass