from django.urls import path
from .views import  book_views,author_views,about_views,BookDetailView,author_create_view,\
  BookDeleteView,BookUpdateView,BookCreateView,krish_views,krish2_views


urlpatterns=[
  path('kutubxona/',book_views,name='books'),
  path('mualliflar/',author_views,name='authors'),
  path('about/',about_views,name='about'),
  path('book/<str:slug>/',BookDetailView.as_view(),name='book_detail'),
  path('kutubxona/book/create',BookCreateView.as_view(),name='book_create'),
  path('kutubxona/author/create',author_create_view,name='author_create'),
  path('book/<str:slug>/delete',BookDeleteView.as_view(),name='book_delete'),
  path('book/<str:slug>/update',BookUpdateView.as_view(),name='book_update'),
  path('krish/',krish_views,name='krish'),
  path('krish2/',krish2_views,name='krish2'),


]