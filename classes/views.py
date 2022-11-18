from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from drf_spectacular.utils import extend_schema

from classes.models import Training, MatchTraining
from classes.serializers import TrainingSerializers, MatchTrainingSerializers


@extend_schema(
    request=TrainingSerializers,
    responses={201: TrainingSerializers},
    description= "Create training"
)
class TrainingViews(viewsets.ModelViewSet):
    serializer_class = TrainingSerializers
    queryset = Training.objects.all()
    pagination_class = PageNumberPagination

@extend_schema(
    request=MatchTrainingSerializers,
    responses={201: MatchTrainingSerializers},
    description= "Verify which student go to training"
)
class MatchTrainingViews(viewsets.ModelViewSet):
    serializer_class = MatchTrainingSerializers
    queryset = MatchTraining.objects.all()
    pagination_class = PageNumberPagination
