from rest_framework import serializers

from .models import Training, MatchTraining


class TrainingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = ["id", "name", "date", "description"]


class MatchTrainingSerializers(serializers.ModelSerializer):
    class Meta:
        model = MatchTraining
        fields = ["id", "study", "training", "status"]
