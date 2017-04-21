from django.db import models
from django.forms import ModelForm

# Create your models here.
class user(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100,default="True")
    state=models.CharField(max_length=100,default="True")
    zipcode=models.IntegerField()
    email=models.EmailField(default="True")
    phone_number=models.IntegerField()
    def __str__(self):
        return self.first_name

class userForm(ModelForm):
    class Meta:
        model = user
        fields =['first_name','last_name','address','city','state','zipcode','email','phone_number']