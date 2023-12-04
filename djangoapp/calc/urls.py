from django.urls import path
from .views import hello, calc, get_users, add_user, login

urlpatterns = [
    # For hello/?x=10
    # path('hello/', hello),
    # For hello/10
    path('hello/<int:number>', hello),
    path('calc', calc),
    path('users', get_users),
    path('adduser', add_user),
    path('login', login),
]