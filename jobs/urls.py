from django.urls import path

from .views import SkillListCreateAPIView, SkillDetailAPIView,JobListCreateAPIView,JobDetailAPIView

urlpatterns = [
    # SKILL APIs
    path('skills/', SkillListCreateAPIView.as_view(), name='skill-list-create'),
    path('skills/<int:pk>/', SkillDetailAPIView.as_view(), name='skill-detail'),

    # JOB APIs
    path('', JobListCreateAPIView.as_view(), name='job-list-create'),
    path('<int:pk>/', JobDetailAPIView.as_view(), name='job-detail'),
]