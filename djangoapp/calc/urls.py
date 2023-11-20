from django.urls import path
from .views import hello, calc

urlpatterns = [
    # For hello/?x=10
    # path('hello/', hello),
    # For hello/10
    path('hello/<int:number>', hello),
    path('calc', calc),
]