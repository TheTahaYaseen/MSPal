from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
 
    path("register", views.register_view, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),    

    path("groups/add", views.add_group_view, name="add_group"),    
    path("groups/update/<str:group_id>", views.update_group_view, name="update_group"),    
    path("groups/delete/<str:group_id>", views.delete_group_view, name="delete_group"),
    
    path("groups/", views.groups_view, name="groups"),    
    path("groups/<str:group_id>", views.group_view, name="group"),    

    path("groups/<str:group_id>/subjects/add", views.add_subject_view, name="add_subject"),    
    path("groups/<str:group_id>/subjects/update/<str:subject_id>", views.update_subject_view, name="update_subject"),    
    path("groups/<str:group_id>/subjects/delete/<str:subject_id>", views.delete_subject_view, name="delete_subject"),    
    
    path("groups/<str:group_id>/subjects/", views.subjects_view, name="subjects"),    
    path("groups/<str:group_id>/subjects/<str:subject_id>", views.subject_view, name="subject"),    

    path("groups/<str:group_id>/subjects/<str:subject_id>/topics/add", views.add_topic_view, name="add_topic"),    
    path("groups/<str:group_id>/subjects/<str:subject_id>/topics/update/<str:topic_id>", views.update_topic_view, name="update_topic"),    
    path("groups/<str:group_id>/subjects/<str:subject_id>/topics/delete/<str:topic_id>", views.delete_topic_view, name="delete_topic"),    
    
    path("groups/<str:group_id>/subjects/<str:subject_id>/topics/cover/<str:topic_id>", views.cover_topic_view, name="cover_topic"),    

    path("groups/<str:group_id>/subjects/<str:subject_id>/topics/", views.topics_view, name="topics"),    
    path("groups/<str:group_id>/subjects/<str:subject_id>/topics/<str:topic_id>", views.topic_view, name="topic"),    

]
