from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class TodosModel(models.Model): #name of the class is the name of the table
    name=models.CharField(max_length=250) #fields of the table
    completed=models.BooleanField(default=False)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,default=None) #delete user's posts when user is deleted
    def __str__(self):
         return self.name
    def get_absolute_url(self):
        return reverse("tododetail",kwargs={"pk":self.pk})
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='',upload_to='')
    def __str__(self):
        return f'{self.user.username} Profile'


