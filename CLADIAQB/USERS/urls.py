from django.urls import path
from .views import register, login, user_detail

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('me/', user_detail, name='user_detail'),
]