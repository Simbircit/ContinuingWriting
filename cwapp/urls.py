from . import views
from django.contrib.auth.urls import path
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.main, name='ContinuingWriting'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_url, name='logout_url'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('create_post/', views.post_create, name='create_post'),
    path('continue_create/', views.continue_create, name='continue_create'),
    path('profile/', views.profile, name='profile'),
    path('like/<post_id>/', views.like_post, name='like_post'),
    path('post_delete/<post_id>', views.post_delete, name='post_delete'),
    path('create_profile/<str:username>', views.create_profile, name='create_profile'),
    path('another_profile/<str:username>', views.another_profile, name='another_profile'),
    path('post/<int:post_id>', views.post_page, name='post'),
    path('post_info/<int:post_id>', views.post_info, name='post_info'),
    path('post_continue/<int:continue_id>', views.post_continue, name='continue'),
    path('password_change_form/',
         auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change_form'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done')
]
