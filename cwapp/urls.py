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
    path('create_profile/<str:username>', views.create_profile, name='create_profile'),
    path('post/<int:post_id>', views.post_page, name='post'),
    path('post_continue/<int:continue_id>', views.post_continue, name='continue')
]
