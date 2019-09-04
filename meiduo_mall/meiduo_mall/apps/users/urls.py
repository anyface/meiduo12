# -*- coding: utf-8 -*-
from . import views
from django.urls import path

urlpatterns = [
    path(r'register/', views.RegisterView.as_view(), name="register")
]