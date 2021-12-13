
from django.db import models
from django.contrib.auth.models import User





# Create your models here.

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=True,blank=True)
    content = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    # parent = models.ForeignKey(blank=True ,null=True, related_name='replies',on_delete=models.CASCADE)
    comments=models.TextField()

    def __str__(self):
        return self.comments









class Course(models.Model):
    subjects = models.CharField(max_length=50,null=True,blank=True)
    name = models.CharField(max_length=50,null=True,blank=True)
    category = models.CharField(max_length=50,null=True,blank=True)
    time = models.CharField(max_length=50,null=True,blank=True)

class Student(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    address = models.CharField(max_length=50,null=True,blank=True)
    age = models.CharField(max_length=50,null=True,blank=True)
    course =models.ForeignKey(Course,null=True,blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
