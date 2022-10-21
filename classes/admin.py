import imp
from django.contrib import admin

from .models import Training, MatchTraining

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ("name", "date", "description")


@admin.register(MatchTraining)
class MatchTrainingAdmin(admin.ModelAdmin):
    list_display = ("study", "status")
