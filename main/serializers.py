from . import models
from rest_framework import serializers


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skill
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Project
        fields = "__all__"
