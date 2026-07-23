from django.urls import path
from .views import RegisterAPIView

urlpatterns = [
    path('Updated/', RegisterAPIView.as_view()),
]