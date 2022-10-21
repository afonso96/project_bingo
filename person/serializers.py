from rest_framework import serializers

from .models import Teacher, Study


class TeacherSerialier(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["id", "name"]


class StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = ["id", "name"]
