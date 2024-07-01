from django.urls import path
from .views import LikeCreateView

urlpatterns = [
    path('', LikeCreateView.as_view()), 
]