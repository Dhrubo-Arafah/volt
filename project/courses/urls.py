from django.urls import path

from courses import views

urlpatterns = [
    path('create-course/<id>', views.create_course, name='create_course')
]
