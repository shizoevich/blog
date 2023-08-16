from django.db import models
from ckeditor.fields import RichTextField 

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    content = RichTextField()

    def __str__(self):
        return self.title