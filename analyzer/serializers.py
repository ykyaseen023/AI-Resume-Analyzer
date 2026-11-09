from rest_framework import serializers
from .models import ResumeAnalysis


class ResumeAnalysisResultSerializer(serializers.ModelSerializer):
    resume_id = serializers.IntegerField(
        source='resume.id',
        read_only=True
    )

    class Meta:
        model = ResumeAnalysis
        fields = [
            'id',
            'resume_id',
            'job',
            'extracted_text',
            'matched_skills',
            'missing_skills',
            'match_score',
            'ai_suggestions',
            'created_at'
        ]