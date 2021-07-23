from django.urls import path
from . import views
from .views import MentorDetailView, MentorUpdateView

urlpatterns = [
    path('', views.register, name='register'),
    path('become-a-mentor/', views.become_a_mentor, name='become_a_mentor'),
    path('mentor-profile/<pk>', MentorDetailView.as_view(), name='mentor_detail_view'),
    path('update-mentor-profile/<pk>', MentorUpdateView.as_view(), name='mentor_update')
]
