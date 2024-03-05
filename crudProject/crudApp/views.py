from django.shortcuts import render , HttpResponseRedirect
from .forms import studentRegistration
from .models import User

# Create your views here.
# This will add a specific entry into the User table.
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

# This will delete a specific student entry from the User table.
def delete_data(request , id):
    if request.method == "POST":
        entry = User.objects.get(id=id)
        entry.delete()
    return HttpResponseRedirect("/crud")

# This will update a specific student entry from the User table
def update_data(request , id):
    student = User.objects.get(id = id)

    if request.method == "POST" : 
        # Iss case mai we don't want ki filled form naye id ke sath table mai save ho jaye so hum django ko bata rahe hai ki yeh student wale entry ke id se associated hai to student id wale entry mai hi iski info ko update krake table mai sve kardena.
        fm = studentRegistration(request.POST , instance=student)

        if fm.is_valid() : 
            fm.save() # yeh shortcut hai otherwise cleaned data nikalo then user object create karo both are same only .
    else :
        # Jab sirf edit pe click hoga so we want ki just empty form na dikhe form ke andar jis bhi entry ko update karna chahte hai uske content ke sath bhara hua form form render hona chahiye . So for that we used instance.
        fm = studentRegistration(instance=student)
    return render(request , "crudApp/updatestudent.html", {"form" : fm , "id" : id})