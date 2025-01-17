from django.urls import path
from .views import RegistrationView, ActivationView, LoginView, RegistrationTemplateView, activation_view, LoginTemplateView, DashboardView, ResetPasswordView, ResetPasswordConfirm
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path('register-api/', RegistrationView.as_view()), 
    path('activate/', ActivationView.as_view()), 
    path('login/', LoginView.as_view()), 
    path('refresh/', TokenRefreshView.as_view()), 
    path('register/', RegistrationTemplateView.as_view(), name='registration'), 
    path('activation/', activation_view, name='activation'), 
    path('login/', LoginTemplateView.as_view(), name='login'), 
    path('dashboard', DashboardView.as_view(), name='dashboard'), 
    path('reset-password/', ResetPasswordView.as_view()), 
    path('reset-password/confirm/', ResetPasswordConfirm.as_view()),

]