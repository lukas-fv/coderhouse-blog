from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.add_category, name='add_category'),
    path('search/', views.search, name='search'),
	path('add_post/', views.add_post, name='add_post'),
]
