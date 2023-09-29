from . import views
from django.urls import path

urlpatterns = [
    path('register', views.Register.as_view()),
    path('login', views.Login.as_view()),
    path('logout', views.Logout.as_view()),
    path('auth',views.UserView.as_view())
]