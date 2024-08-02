from django.shortcuts import render
from .models import Project_Blog
projects=[
        {'title':'ArtDrive','bodycontent':'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Officiis in accusamus architecto suscipit dolorum vero, tempora sapiente eligendi aspernatur nihil.',},
        {'title':'Book Drive','bodycontent':'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Officiis in accusamus architecto suscipit dolorum vero, tempora sapiente eligendi aspernatur nihil.',},
        {'title':'Kulay Kalikasan','bodycontent':'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Officiis in accusamus architecto suscipit dolorum vero, tempora sapiente eligendi aspernatur nihil.',},
]
# Create your views here.
def home(request):
        projectss=Project_Blog.objects.all()
        context={'projects': projectss}
        return render(request,"pages/projectcarousel.html",context)

def project(request, pk):
     
        projectss=Project_Blog.objects.get(title=pk)
       
        context={'blog': projectss}
        return render(request,"pages/readblog.html",context)
