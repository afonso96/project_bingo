from rest_framework import routers

from .views import MatchTrainingViews, TrainingViews

classes_router = routers.DefaultRouter()

classes_router.register("training", viewset=TrainingViews, basename="training")
classes_router.register("matchtraining", viewset=MatchTrainingViews, basename="matchtraining")
