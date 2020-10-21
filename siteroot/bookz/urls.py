from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('newbook/', newbook, name='newbook'),
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>/', BooksByCategory.as_view(), name='category'),
    path('category/zhanry/', GetBook.as_view(), name='book'),
    path('genres/<str:slug>/', BooksByGenre.as_view(), name='genre'),
    path('book/<str:slug>/', GetBook.as_view(), name='book'),
    path('search/', Search.as_view(), name='search'),
]