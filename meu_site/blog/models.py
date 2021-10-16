from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    titulo   = models.CharField(max_length=250)
    slug     = models.SlugField(max_length=250)
    autor    = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    conteudo = models.TextField()
