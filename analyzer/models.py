from django.db import models

# Create your models here.

from django.db import models
from resumes.models import Resume
from jobs.models import Job


class ResumeAnalysis(models.Model):

    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name='analyses'
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='resume_analyses'
    )

    extracted_text = models.TextField(blank=True)

    match_score = models.FloatField(default=0.0)

    matched_skills = models.JSONField(default=list, blank=True)

    missing_skills = models.JSONField(default=list, blank=True)

    ai_suggestions = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis - {self.resume}"