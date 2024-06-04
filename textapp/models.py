from django.db import models
# Create your models here.
class Text(models.Model):
    
    title = models.CharField(max_length=50)
    text = models.TextField()