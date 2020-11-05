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
    path('owner/<str:slug>/', BooksByOwners.as_view(), name='owner'),# добавил чтобы выводить владельца на странице книги
    path('genres/', genres_all, name='all_genres'),#добавил путь чтобы выводить жанры на отдельной странице
    path('about/', about, name='about'),#добавил путь чтобы вывести страницу о сайте
    path('find_book/', books_all, name='find_book'),#добавил путь чтобы выводить поиск книг на отдельной странице
    path('popular/', popular, name='popular'),#добавил путь чтобы выводить популярные книги на отдельной странице
    path('novinki/', novinki, name='novinki'),#добавил путь чтобы выводить недавно добавленные книги на отдельной странице
    path('book/<str:slug>/', GetBook.as_view(), name='book'),#адрес ссылки на отдельную книгу
    path('search/', Search.as_view(), name='search'),
]