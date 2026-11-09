from django.shortcuts import get_object_or_404
from .serializers import ResumeAnalysisResultSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from jobs.models import Job
from .utils import calculate_job_match
from resumes.models import Resume
from .models import ResumeAnalysis
from .utils import identify_resume_skills,generate_ai_suggestions
from google.genai.errors import ServerError

class ResumeSkillAnalysisAPIView(APIView):

    permission_classes = [IsAuthenticated]

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

        if not analysis.extracted_text.strip():
            return Response(
        {
            "error": "No text found in this resume. Please upload a valid PDF or DOCX file."
        },
        status=status.HTTP_400_BAD_REQUEST
        )

        matched_skills = identify_resume_skills(
            analysis.extracted_text
        )

        analysis.matched_skills = matched_skills
        analysis.save()

        return Response({
            "message": "Resume skills identified successfully",
            "resume_id": resume.id,
            "matched_skills": matched_skills,
            "total_skills_found": len(matched_skills)
        }, status=status.HTTP_200_OK)

class ResumeJobMatchAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, resume_id, job_id):

        resume = get_object_or_404(
            Resume,
            id=resume_id,
            user=request.user
        )

        job = get_object_or_404(
            Job,
            id=job_id,
            is_active=True
        )

        analysis = get_object_or_404(
            ResumeAnalysis,
            resume=resume
        )

        if not analysis.matched_skills:
            return Response(
        {
            "error": "Identify resume skills before matching with a job."
        },
        status=status.HTTP_400_BAD_REQUEST
    )

        result = calculate_job_match(
            analysis.matched_skills,
            list(job.required_skills.values_list(
                'name', flat=True
            ))
        )

        analysis.job = job
        analysis.match_score = result["match_score"]
        analysis.matched_skills = result["matched_skills"]
        analysis.missing_skills = result["missing_skills"]

        analysis.save()

        return Response({
            "message": "Resume and job matching completed",
            "resume_id": resume.id,
            "job_id": job.id,
            **result
        }, status=status.HTTP_200_OK)

class ResumeAIAnalysisAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, resume_id):

        # Get the resume belonging to the logged-in user
        resume = get_object_or_404(
            Resume,
            id=resume_id,
            user=request.user
        )

        # Get the extracted resume analysis
        analysis = get_object_or_404(
            ResumeAnalysis,
            resume=resume
        )

        # Check whether resume text is available
        if not analysis.extracted_text.strip():
            return Response(
                {"error": "Resume text is empty. Upload the resume again."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Send resume text to Gemini
        try:
            suggestions = generate_ai_suggestions(
        analysis.extracted_text
    )

        except ServerError:
            return Response(
        {
            "error": "Gemini AI is temporarily busy. Please try again in a minute."
        },
        status=status.HTTP_503_SERVICE_UNAVAILABLE
    )

        # Save AI suggestions in MySQL
        analysis.ai_suggestions = suggestions
        analysis.save()

        return Response({
            "message": "AI resume analysis completed successfully",
            "resume_id": resume.id,
            "ai_suggestions": suggestions
        }, status=status.HTTP_200_OK)

class ResumeAnalysisResultAPIView(APIView):
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

        serializer = ResumeAnalysisResultSerializer(analysis)

        return Response(serializer.data, status=status.HTTP_200_OK)