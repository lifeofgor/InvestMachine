from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.AboutOurCompany, name='about'),
    path('', views.NewsPage, name='News'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='detail'),

]