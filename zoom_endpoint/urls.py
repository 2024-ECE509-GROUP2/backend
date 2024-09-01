from django.urls import path

from . import views

urlpatterns = [
    path('redirect', views.generate_signature, name="generate"),
    path('meeting/', views.get_meetings, name="list_meeting"),
    path('meeting/<int:pk>', views.get_meetings, name="list_meeting"),
    path('meeting/join', views.join_meeting, name="join_meeting"),
    path('meeting/start', views.start_meeting, name="start_meeting"),
    path('meeting/create', views.create_meeting, name="create_meeting"),
]
