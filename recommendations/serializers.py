from rest_framework import serializers
from .models import CareerRecommendation


class CareerRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerRecommendation
        fields = [
            'id',
            'career_title',
            'match_score',
            'reason',
            'suggested_skills',
            'created_at'
        ]