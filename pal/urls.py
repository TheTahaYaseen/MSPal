from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
 
    path("register", views.register_view, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),    

    path("groups/", views.groups_view, name="groups"),    
    path("groups/<str:group_id>", views.group_view, name="group"),    

    path("groups/add", views.add_group_view, name="add_group"),    
    path("groups/update/<str:group_id>", views.update_group_view, name="update_group"),    
    path("groups/delete/<str:group_id>", views.delete_group_view, name="delete_group"),

]
