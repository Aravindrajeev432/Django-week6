
from ast import Pass
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.cache import cache_control
from .models import Home, Users,UserDetails
import sys
from django.contrib import messages
# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    if 'username' in request.session:
        return redirect(home)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        print(username)
        print(password)
        # Raw Query
        user_log=Users.objects.raw('SELECT login_system_users.uid,login_system_users.user_name,login_system_users.passw FROM login_system_users')
        print("size of raw query variable is", end='')
        print(sys.getsizeof(user_log))
        print(user_log)
        for i in user_log:
            print(i.uid,end='-')
            print(i.user_name,end='-')
            print(i.passw)
            if username==i.user_name and password==i.passw:
                
                print("successs")
                #create session
                request.session['username']=i.user_name
                request.session['uid']=i.uid
                print(i.user_name)
                print(i.uid)
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
    if 'username' in request.session:
        return redirect(home)
    print("reg")
    if request.method == 'POST':
        
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        uname = request.POST.get('uname')
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
        e_user=Users.objects.all()
        for e in e_user:
            if e.user_name==uname:
                messages.info(request, 'Username already existed .Pick another one')
                return redirect(reg)
            else:
                user_tabel=Users(first_name=fname,last_name=lname,user_name=uname,email=email,phone=phone,passw=passw,address=address,city=city,state=staten,zip=zip)
                user_tabel.save()
        # user_cre = UserDetails(user_name=uname)
        # user_cre.save()
        return redirect(index)

    return render(request,'reg.html')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if 'username' in request.session:
        print("home")
        # user_details = Users.objects.all()
        # home_details = Home.objects.only("location")
        # for k in home_details:
        #     print(k.location)
        home_details = Home.objects.all()
        # for h in home_details:
        #     print(type(h.image))
        return render(request,'home.html',{'username':request.session['username'],'userid':request.session['uid'],'home_info':home_details})
   
    else:return redirect(index)
        
    

def logout(request):
    request.session.flush()
    return redirect(index)