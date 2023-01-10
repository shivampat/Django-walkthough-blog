from django.db import models
from datetime import datetime

# Create your models here.
class BlogPost(models.Model):
    blogTitle = models.CharField(max_length=50)
    blogDateTime = models.DateTimeField(default=datetime.now())
    blogText = models.TextField(null=False, blank=False)
    blogMonth = models.IntegerField(null=True, default=datetime.now().month)
    blogYear = models.IntegerField(null=True, default=datetime.now().year)