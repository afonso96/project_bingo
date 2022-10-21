from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .serializers import TeacherSerialier, StudySerializer
from .models import Teacher, Study


class TeacherViews(viewsets.ModelViewSet):
    serializer_class = TeacherSerialier
    queryset = Teacher.objects.all()
    pagination_class = PageNumberPagination


class StudyViews(viewsets.ModelViewSet):
    serializer_class = StudySerializer
    queryset = Study.objects.all()
    pagination_class = PageNumberPagination