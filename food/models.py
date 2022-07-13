import imp
from pyexpat import model
from django.db import models

#Import User model

from django.contrib.auth.models import User

#importing reverse

from django.urls import reverse

# Create your models here.

class Item(models.Model):
    
    def __str__(self):
        return self.item_name
    
    #Assosiating User model with Item model. 
    #To do this we have to make one model as foreign  key in another. Lets do it.



    user_name=models.ForeignKey(User,on_delete=models.CASCADE,default=1)


    item_name=models.CharField(max_length=200)
    item_desc=models.CharField(max_length=200)
    item_price=models.IntegerField()
    item_image=models.CharField(max_length=500,default="https://c8.alamy.com/comp/B3C2XG/taking-a-slice-of-pizza-B3C2XG.jpg")

    def  get_absolute_url(self):
        return reverse("food:detail",kwargs={"pk":self.pk})