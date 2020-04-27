from django.urls import path
from . import views

urlpatterns = [
    path('', views.Postview.as_view(),name='blog-home'),
    path('post/new/', views.PostCreateview.as_view(),name='post-create'),
    path('post/<int:pk>/', views.PostDetailview.as_view(), name='post-detail'),
    path('post/<int:pk>/update', views.PostUpdateview.as_view(), name='post-update'),
    path('post/<int:pk>/delete', views.PostDeleteview.as_view(), name='post-delete'),
    path('user/<str:username>/', views.UserPostview.as_view(), name='user-post'),
    path('about/', views.about, name='blog-about'),
]