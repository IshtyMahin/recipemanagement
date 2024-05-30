from django.db import models

# Create your models here.
from member.models import Member

class Ingredients(models.Model):
    name = models.CharField(max_length=255)
    
class Recipes(models.Model):
    recipe_name = models.CharField(max_length=255)
    steps_of_recipe = models.TextField()
    ingredients = models.ManyToManyField(Ingredients)
    chief = models.ForeignKey(Member,on_delete=models.CASCADE)
    
    

class Ratings(models.Model):

    rating = models.IntegerField()
    recipe = models.ForeignKey(Recipes,on_delete=models.CASCADE)
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    
    
    
class Comments(models.Model):
    comment = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    recipe = models.ForeignKey(Recipes,on_delete=models.CASCADE)
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    
    