from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from resumes.models import Resume
from analyzer.models import ResumeAnalysis
from analyzer.utils import calculate_job_match
from jobs.models import Job
from .models import CareerRecommendation
from .serializers import CareerRecommendationSerializer


class CareerRecommendationAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, resume_id):
        resume = get_object_or_404(
            Resume,
            id=resume_id,
            user=request.user
        )

        analysis = get_object_or_404(
            ResumeAnalysis,
            resume=resume
        )

        recommendations = analysis.career_recommendations.all().order_by(
            '-match_score'
        )

        serializer = CareerRecommendationSerializer(
            recommendations,
            many=True
        )

        return Response(serializer.data)

    def post(self, request, resume_id):
        resume = get_object_or_404(
            Resume,
            id=resume_id,
            user=request.user
        )

        analysis = get_object_or_404(
            ResumeAnalysis,
            resume=resume
        )

        if not analysis.matched_skills:
            return Response(
                {
                    "error": "Identify resume skills first."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        jobs = Job.objects.filter(
            is_active=True
        ).prefetch_related('required_skills')

        if not jobs.exists():
            return Response(
                {"message": "No active jobs available."},
                status=status.HTTP_200_OK
            )

        # Remove old recommendations before creating new ones.
        analysis.career_recommendations.all().delete()

        new_recommendations = []

        for job in jobs:
            required_skills = list(
                job.required_skills.values_list('name', flat=True)
            )

            result = calculate_job_match(
                analysis.matched_skills,
                required_skills
            )

            if result["match_score"] == 0:
                continue

            matched = result["matched_skills"]
            missing = result["missing_skills"]

            reason = (
                f"You match {len(matched)} required skills: "
                f"{', '.join(matched)}. "
            )

            if missing:
                reason += (
                    f"Learn these skills to improve your fit: "
                    f"{', '.join(missing)}."
                )
            else:
                reason += "You have all the listed required skills."

            recommendation = CareerRecommendation(
                analysis=analysis,
                career_title=job.title,
                match_score=result["match_score"],
                reason=reason,
                suggested_skills=missing
            )

            new_recommendations.append(recommendation)

        CareerRecommendation.objects.bulk_create(
            new_recommendations
        )

        recommendations = analysis.career_recommendations.all().order_by(
            '-match_score'
        )

        serializer = CareerRecommendationSerializer(
            recommendations,
            many=True
        )

        return Response(
            {
                "message": "Career recommendations generated successfully",
                "total_recommendations": len(new_recommendations),
                "recommendations": serializer.data
            },
            status=status.HTTP_200_OK
        )