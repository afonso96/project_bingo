from rest_framework import routers

from .views import TeacherViews, StudyViews

person_routers = routers.DefaultRouter()

person_routers.register("teacher", viewset=TeacherViews, basename="teacher")
person_routers.register("study", viewset=StudyViews, basename="study")
