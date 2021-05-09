from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.login.views import AccederView, RegisterUserView, CopyrightView

app_name = 'login'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', AccederView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='book:home'), name='logout'),
    path('copyright/', CopyrightView.as_view(), name='copyright'),
]