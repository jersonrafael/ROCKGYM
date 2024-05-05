from django.urls import path
from .views import *

urlpatterns = [
	path("", clientsView.as_view()),
	path("client/<int:pk>", clientView.as_view()),
]