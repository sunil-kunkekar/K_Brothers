from django.db import models
import uuid

# Create your models here.
class POST(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=500, null=True)
    url = models.URLField(max_length=500, null=True) 
    image = models.URLField(max_length=100)
    tags = models.ManyToManyField('Tag')
    body  = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    id  = models.CharField(max_length=100,default=uuid.uuid4, unique=True,primary_key=True,editable=False)
    
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_at']
        

class Tag(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)
    
    def __str__(self):
        return self.name