from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(blank=True, null=True)
    compile_post = models.BooleanField(default=False)  
      
    def publish(self):
        self.created_date=timezone.now()
        self.save()
        
    def __str__(self):
        return self.title
