from django.db import models

# Create your models here.
class Author(models.Model):  
    name = models.CharField(max_length= 100)

    def _str_(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length = 100)
    publication_year = models.IntegerField()
    
    #link the two models with a one to two relationship(foreignkey)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='Books')
    
    def _str_(self):
        return self.title