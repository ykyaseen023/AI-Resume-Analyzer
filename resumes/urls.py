from django.urls import path
from .views import (
    ResumeUploadAPIView,
    ResumeListAPIView,
    ResumeDeleteAPIView
)

urlpatterns = [
    path('upload/', ResumeUploadAPIView.as_view(), name='resume-upload'),
    path('list/', ResumeListAPIView.as_view(), name='resume-list'),
    path('<int:pk>/delete/', ResumeDeleteAPIView.as_view(), name='resume-delete'),
]