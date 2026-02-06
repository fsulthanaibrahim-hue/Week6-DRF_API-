from django.urls import path, include
from .views import StudentAPIView


urlpatterns = [
    path('students/', StudentAPIView.as_view(), name='students'),
    path('students/<int:pk>/', StudentAPIView.as_view(), name='student-detail'),
]