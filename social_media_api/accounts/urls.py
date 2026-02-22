from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView # Assuming you made a RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
]