from django.urls import path

from .views import ResumeSkillAnalysisAPIView,ResumeJobMatchAPIView,ResumeAIAnalysisAPIView,ResumeAnalysisResultAPIView


urlpatterns = [
    path(
        'resumes/<int:resume_id>/identify-skills/',
        ResumeSkillAnalysisAPIView.as_view(),
        name='identify-resume-skills'
    ),

    path(
        'resumes/<int:resume_id>/match/<int:job_id>/',
        ResumeJobMatchAPIView.as_view(),
        name='resume-job-match'
    ),

    path(
    'resumes/<int:resume_id>/ai-analysis/',
    ResumeAIAnalysisAPIView.as_view(),
    name='resume-ai-analysis'
    ),

    path(
    'resumes/<int:resume_id>/result/',
    ResumeAnalysisResultAPIView.as_view(),
    name='resume-analysis-result'
),
]