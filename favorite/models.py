from django.db import models
from menu.models import Menu
from django.contrib.auth import get_user_model
from comment.models import Comment

User = get_user_model() 

class Favorite(models.Model):
    menu = models.ForeignKey(Menu, related_name='favorites', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)

class Like(models.Model):
    comment = models.ForeignKey(Comment, related_name='likes', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
