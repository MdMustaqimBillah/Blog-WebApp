from Blog_App import views
from django.urls import path
from Blog_App import views

app_name = 'Blog_App'

urlpatterns = [
   path('', views.IndexView.as_view(), name='index'),
   path('post/', views.Post.as_view(), name='post'),
   path('user_posts/', views.user_posts, name='user_posts'),
   path('post_details/<slug>/', views.post_details, name='post_details'),
   path('user_post_details/<slug>/', views.user_post_details, name='user_post_details'),
   path('update_post/<slug>/', views.UpdatePost.as_view(), name='update_post'),
   path('delete_post/<slug>/', views.PostDeleteView.as_view(), name='delete_post'),
   path('like_post/<int:pk>/', views.like, name='like_post'),
   path('undo_like/<int:pk>/', views.undo_like, name='undo_like'),
   path('change_comment/<int:pk>/', views.EditComment.as_view(), name='change_comment'),
   path('delete_comment/<int:pk>/', views.delete_comment, name='delete_comment')

]