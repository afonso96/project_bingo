from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from classes.models import Training, MatchTraining
from classes.serializers import TrainingSerializers, MatchTrainingSerializers


class TrainingViews(viewsets.ModelViewSet):
    serializer_class = TrainingSerializers
    queryset = Training.objects.all()
    pagination_class = PageNumberPagination


class MatchTrainingViews(viewsets.ModelViewSet):
    serializer_class = MatchTrainingSerializers
    queryset = MatchTraining.objects.all()
    pagination_class = PageNumberPagination
