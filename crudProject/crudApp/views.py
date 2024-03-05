from django.shortcuts import render , HttpResponseRedirect
from .forms import studentRegistration
from .models import User

# Create your views here.
def addandshow(request):
    if request.method == "POST":
        fm = studentRegistration(request.POST)

        if fm.is_valid():
            name = fm.cleaned_data["name"] 
            email = fm.cleaned_data["email"] 
            password = fm.cleaned_data["password"] 

            print(name,email,password)

            regis = User(name=name,email=email,password=password)
            regis.save()
            fm = studentRegistration()
    else:
        fm = studentRegistration()

    students = User.objects.all()
    return render(request , "crudApp/addandshow.html" , {"form" : fm , "stu" : students})

def delete_data(request , id):
    if request.method == "POST":
        entry = User.objects.get(id=id)
        entry.delete()
    return HttpResponseRedirect("/crud")
