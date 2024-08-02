from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name="home"),
    path('projects/<str:pk>',views.project,name="project")
]
