from django.urls import path, include
from . import views

urlpatterns = [
    path(r'',views.form_method,name="form_method"),
    path(r'dashboard/',views.dashboard,name="dashboard"),
    path(r'admin/',views.admin,name="admin"),
    path('export-csv/',views.ExportCsvView.as_view(),name="export_csv")
]