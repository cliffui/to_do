from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.dashboard,name="dashboard"),
    path("login",views.login,name="login"),
    path("register",views.register,name="register"),
    path("logout",auth_views.LogoutView.as_view(template_name="logged_out.html"),name="logout"),
    path("edit/<list_id>",views.edit,name="edit"),
    path("edit_record/<list_id>",views.edit_record,name="edit_record"),
    path("delete/<list_id>",views.delete,name="delete"),
]
