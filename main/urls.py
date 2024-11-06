from django.urls import path 
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("details/<int:id>",views.details,name="details"),
    path("<int:id>",views.index1,name="index"),
]
