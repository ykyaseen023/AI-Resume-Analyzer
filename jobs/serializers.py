from rest_framework import serializers
from .models import Skill, Job


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):

    required_skills = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Skill.objects.all()
    )

    class Meta:
        model = Job
        fields = '__all__'