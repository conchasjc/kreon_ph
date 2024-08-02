from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.

class Project_Blog(models.Model):
    title=models.CharField(max_length=200,null=False,blank=False)
    bodycontent=RichTextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title