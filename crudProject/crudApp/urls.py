from django.urls import path
from crudApp import views

urlpatterns = [
    path("" , views.addandshow , name="addandshow"),
]