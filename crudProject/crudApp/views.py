from django.shortcuts import render

# Create your views here.
def addandshow(request):
    return render(request , "crudApp/addandshow.html")