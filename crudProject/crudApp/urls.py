from django.urls import path
from crudApp import views

urlpatterns = [
    path("" , views.addandshow , name="addandshow"),
    path("delete/<int:id>" , views.delete_data , name="deletedata")
]