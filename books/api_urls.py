from django.urls import path
from . import api
urlpatterns=[path('books/',api.BookListCreate.as_view()),path('books/<int:pk>/',api.BookDetail.as_view()),path('categories/',api.CategoryList.as_view()),path('favorites/',api.FavoriteCreate.as_view()),path('favorites/<int:pk>/',api.UserFavoriteDelete.as_view()),path('messages/',api.MessageCreate.as_view())]
