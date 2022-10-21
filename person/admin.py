from django.contrib import admin
from .models import Teacher, Study


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    list_display = ("name",)
