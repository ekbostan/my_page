from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Post(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    content = models.TextField(MinLengthValidator(30))
    importance = models.PositiveSmallIntegerField()
    github = models.URLField()
    explanation = models.TextField()

    def __str__(self):
        return f"{self.title}"

        