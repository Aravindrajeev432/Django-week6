
from ast import Pass
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.cache import cache_control
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
def home(request):
    print("home")
    if request.method == 'POST':
        inp = request.POST['inp']
        print(inp)
        return render(request,'home.html')

    return render(request,'home.html')

def logout(request):
    return Pass