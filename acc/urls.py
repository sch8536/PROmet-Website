from django.urls import path
from acc import views
from django.contrib.auth import views as auth_views

app_name = 'acc'

urlpatterns = [
  path('profile/', views.profile, name='profile'),
  path('login/', auth_views.LoginView.as_view(template_name='acc/login.html'), name='login'),
  path('signup/', views.signup, name='signup'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout')
]