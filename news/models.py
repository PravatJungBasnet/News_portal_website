from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='img')
    def __str__(self):
        return self.title
 
class news(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='news_img')
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural='news'
    



