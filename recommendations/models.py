from django.db import models

# Create your models here.
from django.db import models
from analyzer.models import ResumeAnalysis


class CareerRecommendation(models.Model):

    analysis = models.ForeignKey(
        ResumeAnalysis,
        on_delete=models.CASCADE,
        related_name='career_recommendations'
    )

    career_title = models.CharField(max_length=150)

    match_score = models.FloatField(default=0.0)

    reason = models.TextField(blank=True)

    suggested_skills = models.JSONField(default=list, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.career_title