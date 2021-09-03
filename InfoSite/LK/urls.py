from django.urls import path, include
from . import views
from .models import User
from django.contrib.auth import views as authViews


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('exit/', authViews.LogoutView.as_view(next_page='login'), name='exit'),
    path('register/',views.register, name='register'),
    path('update_account/', views.edit, name='update'),
    path('profile/', views.PersonalPage, name='profile'),
    path('add/', views.AddNews, name='add')

]