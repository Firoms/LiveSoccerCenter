from django.db import models
from user.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=80, null=False)
    content = models.TextField(null=False)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    delete = models.BooleanField(default=False)
    files = models.FileField(upload_to='uploads/%Y/%m/%d/', max_length=None, null=True, blank=True) # None 안될 시 100

    def __str__(self):
        return f"{self.id}. {self.title}"
    

class Comment(models.Model):
    content = models.CharField(max_length=80, null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    delete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}. {self.content}"