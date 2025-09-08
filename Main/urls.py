from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("services/", views.services_list, name="services_list"),
    path("laptops/", views.laptops_list, name="laptops_list"),
    path("accessories/", views.accessories_list, name="accessories_list"),
    path("About_Us", views.aboutus, name="about_us"),
    path("Contact", views.contactus, name="contact_us"),
    path("search/", views.search_view, name="search"),

]
