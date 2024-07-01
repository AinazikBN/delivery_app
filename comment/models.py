from django.db import models
from menu.models import Menu
from django.contrib.auth import get_user_model

User = get_user_model() 

class Comment(models.Model):
    owner = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return f'{self.owner} > {self.menu}'

