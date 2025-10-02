from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 

app_name = "modelform"

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/',views.CustomSignupView.as_view(), name="signup"),
    path('login/',views.CustomLoginView.as_view(),name="login")
    
]