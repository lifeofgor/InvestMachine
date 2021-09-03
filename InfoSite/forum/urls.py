from django.urls import path
from . import views


urlpatterns = [
    path('', views.ForumPage, name='forum'),
    path('<int:pk>', views.DetailForum.as_view(), name='detailforum'),
    path('<int:pk>/deletepost/', views.PostDeleteView.as_view(), name='deletepost'),
    path('<int:pk>/deletecomment/', views.CommentDeleteView.as_view(), name='deletecomment'),
]