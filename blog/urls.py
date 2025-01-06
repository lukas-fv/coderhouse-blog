from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/add', views.add_category, name='add_category'),
    path('search/', views.search, name='search'),
	path('add_post/', views.add_post, name='add_post'),
	path('about_me/', views.about_me, name="about_me"),
	path('post/<slug:slug>/', views.post_detail, name='post_detail'),
	path('recursos/', views.recursos, name="recursos"),
	path('register/', views.register, name='register'),
	path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
	path('accounts/profile/', views.profile, name="profile"),
]
