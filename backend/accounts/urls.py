from django.urls import path, re_path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    re_path(r'^auth/obtain_token/', obtain_jwt_token, name='jwt-auth'),
    re_path(r'^auth/refresh_token/', refresh_jwt_token, name='jwt-refresh'),
    re_path(r'^auth/verify_token/', verify_jwt_token, name='jwt-verify'),
]