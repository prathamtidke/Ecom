from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
    path ("", views.index , name = "Shop Home"),
    path ("home", views.index , name = "Shop Home"),
    path ("about",views.about,name = "About"),
    path ("contact",views.contact,name = "Contactus"),
    path ("tracking",views.tracking,name = "Tracking"),


]
