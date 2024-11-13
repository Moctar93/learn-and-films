from django.urls import path
from users.views import RegisterView, UserListView, CustomAuthToken, user_dashboard

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('user/dashboard/', user_dashboard, name='user_dashboard')
]

