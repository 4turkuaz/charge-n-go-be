from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("users/", views.Users.as_view()),
    path("users/<uuid:pk>/", views.UserDetails.as_view()),
    path("login/", views.Login.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
