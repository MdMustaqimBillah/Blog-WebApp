from Blog_App import views
from django.urls import path

app_name = 'Blog_App'

urlpatterns = [
   path('', views.index, name='index'),

]