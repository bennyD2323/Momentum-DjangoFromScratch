from django.db import models
from users.models import User
from django.db.models import Q



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

    def get_tag_names(self):
        tag_names = []
        for tag in self.tags.all():
            tag_names.append(tag.tag)
        return " ".join(tag_names)

    def set_tag_names(self, tag_names):
        tag_names = tag_names.split()
        tags = []
        for tag_name in tag_names:
            tag = Tag.objects.filter(tag=tag_name).first()
            if tag is None:
                tag = Tag.objects.create(tag=tag_name)
            tags.append(tag)
        self.tags.set(tags)

    def __str__(self):
        return self.title


# def search_snippets_for_user(user, query):
#     return user.snippets.filter(
#         Q(title__icontains=query) | Q(tags__tag__icontains=query)).distinct()
