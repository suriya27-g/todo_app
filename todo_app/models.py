from django.db import models

# Create your models here.
class List_View(models.Model):
    items = models.CharField(max_length=150)
    
    def __str__(self):
        return self.items