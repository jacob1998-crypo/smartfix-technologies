from django.shortcuts import render
from .models import Service
from .models import Laptop
from .models import Accessory
from django.db.models import Q


def home(request):
    return render(request, "home/index.html")


def services_list(request):
    services = Service.objects.all()
    return render(request, "pages/services.html", {"services": services})



def laptops_list(request):
    laptops = Laptop.objects.all().order_by("-created_at")
    return render(request, "pages/laptops.html", {"laptops": laptops})


def accessories_list(request):
    accessories = Accessory.objects.all().order_by("-created_at")
    return render(request, "pages/accessories.html", {"accessories": accessories})



def aboutus(request):
    return render(request,"pages/aboutus.html")

def contactus(request):
    return render(request,"pages/contact.html")




def search_view(request):
    query = request.GET.get("q", "").strip()
    filter_type = request.GET.get("type", "all")  
    results = []

    if query:
        if filter_type in ("all", "laptops"):
            laptops = Laptop.objects.filter(
                Q(name__icontains=query) |
                Q(specs__icontains=query)
            )
            for item in laptops:
                results.append({
                    "type": "Laptop",
                    "name": item.name,
                    "details": item.specs,
                    "price": item.price,
                    "image": item.image.url if item.image else None,
                })

        if filter_type in ("all", "accessories"):
            accessories = Accessory.objects.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )
            for item in accessories:
                results.append({
                    "type": "Accessory",
                    "name": item.name,
                    "details": item.description,
                    "price": item.price,
                    "image": item.image.url if item.image else None,
                })

        if filter_type in ("all", "services"):
            services = Service.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )
            for item in services:
                results.append({
                    "type": "Service",
                    "name": item.title,
                    "details": item.description,
                    "price": None,  # services don’t have price in your model
                    "image": item.image.url if item.image else None,
                })

    return render(request, "pages/search.html", {
        "query": query,
        "results": results,
        "filter_type": filter_type,
    })

