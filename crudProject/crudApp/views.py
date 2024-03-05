from django.shortcuts import render
from .forms import studentRegistration

# Create your views here.
def addandshow(request):
    if request.method == "POST":
        fm = studentRegistration(request.POST)
        print("Yes it worked..")
    else:
        fm = studentRegistration()
    return render(request , "crudApp/addandshow.html" , {"form" : fm})