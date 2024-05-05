from django.urls import path
from .views import *

urlpatterns = [
    path('classes/', classesView.as_view()),
    path('class/<int:pk>/', classView.as_view()),
]
