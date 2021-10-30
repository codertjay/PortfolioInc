from django.urls import path
from .views import (BlogListView,
                    BlogDetailView,
                    DeletePostView,
                    create_comment,
                    blog_user_list_view
                    )

app_name = 'blog'
urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('#/#/<str:username>/', blog_user_list_view, name='blog_user_list'),
    path('<str:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('<str:slug>/create_comment/', create_comment, name='blog_comment'),
    path('<str:slug>/delete/', DeletePostView.as_view(), name='delete_post'),
]
