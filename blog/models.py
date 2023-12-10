from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=50)
    pub_date = models.DateTimeField()

    def __str__(self):
        return f"{self.title} {self.content} {self.category} {self.pub_date}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    content = models.TextField()
    pos_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user_id} on {self.post_id}"

class Category(models.Model):
    title_category = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title_category}"
