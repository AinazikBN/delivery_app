from django.db import models
from django.contrib.auth import get_user_model
from menu.models import Menu

User = get_user_model()

class Rating(models.Model):
    RATING_CHOICES = (
        (1, 'Too bad'), 
        (2, 'Bad'),
        (3, 'Normal'), 
        (4, 'Good'), 
        (5, 'Excellent'), 
    )

    menu = models.ForeignKey(Menu, related_name='ratings', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['owner', 'menu']
