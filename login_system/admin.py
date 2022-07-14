from django.contrib import admin
from .models import Users,Home
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","email","phone","address","city","state","zip")
    search_fields= ['first_name','email','city','state','phone']
admin.site.register(Users,UserAdmin)
class HomeAdmin(admin.ModelAdmin):
    list_display=("location","contact","zip","price","image")

admin.site.register(Home,HomeAdmin)
