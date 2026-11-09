from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import ListAPIView
from rest_framework.generics import DestroyAPIView
from analyzer.models import ResumeAnalysis
from .utils import extract_resume_text
from .models import Resume
from .serializers import ResumeSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from resumes.models import Resume
from resumes.serializers import ResumeSerializer
from analyzer.models import ResumeAnalysis
from resumes.utils import extract_resume_text


class ResumeUploadAPIView(CreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):

        # Save the resume with the logged-in user
        resume = serializer.save(user=self.request.user)

        # Extract text from the uploaded file
        extracted_text = extract_resume_text(resume.file.path)

        # Save extracted text in ResumeAnalysis table
        ResumeAnalysis.objects.create(
            resume=resume,
            extracted_text=extracted_text
        )

class ResumeListAPIView(ListAPIView):

    serializer_class = ResumeSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user).order_by('-uploaded_at')



class ResumeDeleteAPIView(DestroyAPIView):

    serializer_class = ResumeSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user)

    def perform_destroy(self, instance):

        instance.file.delete(save=False)

        instance.delete()