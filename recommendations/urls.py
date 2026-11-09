from django.urls import path
from .views import CareerRecommendationAPIView

urlpatterns = [
    path(
        'resumes/<int:resume_id>/career-recommendations/',
        CareerRecommendationAPIView.as_view(),
        name='career-recommendations'
    ),
]