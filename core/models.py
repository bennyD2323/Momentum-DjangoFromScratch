from django.db import models
from users.models import User



class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag

# Create your models here.
class CodeSnippet(models.Model):
    body = models.TextField()
    title = models.CharField(max_length=30)
    tags = models.ManyToManyField(to=Tag, related_name='snippets')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="snippets")
    language = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    parent = models.ForeignKey(to='self', on_delete=models.SET_NULL, related_name="children", null=True, blank=True)

    def __str__(self):
        return self.title



