from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .permissions import IsAdminOrReadOnly
from .models import Skill, Job
from .serializers import SkillSerializer, JobSerializer


class SkillListCreateAPIView(ListCreateAPIView):

    queryset = Skill.objects.all().order_by('name')

    serializer_class = SkillSerializer

    permission_classes = [IsAdminOrReadOnly]


class SkillDetailAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Skill.objects.all()

    serializer_class = SkillSerializer

    permission_classes = [IsAdminOrReadOnly]



class JobListCreateAPIView(ListCreateAPIView):

    queryset = Job.objects.filter(is_active=True).order_by('-created_at')

    serializer_class = JobSerializer

    permission_classes = [IsAdminOrReadOnly]


class JobDetailAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Job.objects.all()

    serializer_class = JobSerializer

    permission_classes = [IsAdminOrReadOnly]