    path("subjects/", views.subjects_view, name="subjects"),    

    path("subjects/update/<str:subject_id>", views.update_subject_view, name="update_subject"),    
    path("subjects/delete/<str:subject_id>", views.delete_subject_view, name="delete_subject"),

, "topics": topics
    topics = Topic.objects.filter(associated_subject=subject)
