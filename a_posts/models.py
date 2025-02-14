from django.db import models
import uuid

# Create your models here.
class POST(models.Model):
    title = models.CharField(max_length=100)
    image = models.URLField(max_length=100)
    body  = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    id  = models.CharField(max_length=100,default=uuid.uuid4, unique=True,primary_key=True,editable=False)
    
    def __str__(self):
        return self.title