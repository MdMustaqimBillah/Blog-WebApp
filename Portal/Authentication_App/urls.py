from django.urls import path
from Authentication_App import views


app_name = 'Authentication_App'

urlpatterns =[
    path('signup/', views.user_signup , name='signup'),
    path('login/', views.user_login , name='login'),
    path('logout/', views.logout_user , name='logout'),
    path('user_profile/', views.user_profile , name='user_profile'),
    path('update_dp/', views.update_dp, name='update_dp'),
    path('update_profile/', views.update_profile , name='update_profile'),
    path('delete_dp/', views.delete_dp, name='delete_dp'),
    path('change_password/', views.change_password, name='change_password'),
    path('delete_account/', views.delete_account, name='delete_account'),

]

