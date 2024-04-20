from django.db import models

# Create your models here.
class Categorie(models.Model):
    name = models.CharField(max_length = 20)
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    description = models.TextField()
    Create_date= models.DateTimeField(auto_now_add = True)
    tags= models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/")
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title