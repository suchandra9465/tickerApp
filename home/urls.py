from django.urls import path, include
from . import views

urlpatterns = [
    path(r'',views.form_method,name="form_method"),
    path(r'dashboard/',views.dashboard,name="dashboard")
]