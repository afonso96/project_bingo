from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from drf_spectacular.utils import extend_schema


from .serializers import TeacherSerialier, StudySerializer
from .models import Teacher, Study

@extend_schema(
    request=TeacherSerialier,
    responses={201: TeacherSerialier},
    description= "Create student"
)
class TeacherViews(viewsets.ModelViewSet):
    serializer_class = TeacherSerialier
    queryset = Teacher.objects.all()
    pagination_class = PageNumberPagination

@extend_schema(
    request=StudySerializer,
    responses={201: StudySerializer},
    description= "Create student"
)
class StudyViews(viewsets.ModelViewSet):
    serializer_class = StudySerializer
    queryset = Study.objects.all()
    pagination_class = PageNumberPagination