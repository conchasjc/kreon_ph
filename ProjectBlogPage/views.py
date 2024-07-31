from django.shortcuts import render

# Create your views here.
def home(request):
    projects=[
        {"title":"Art Drive"},
        {"title":"Art Drive"},
        {"title":"Art Drive"},
        ]
    return render(request,"pages/projectcarousel.html")