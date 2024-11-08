from django.shortcuts import render
from . import models, serializers
from rest_framework import viewsets


class SkillViewSet(viewsets.ModelViewSet):
    queryset = models.Skill.objects.all()
    serializer_class = serializers.SkillSerializer
    http_method_names = ['get']


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    http_method_names = ['get']


# Create your views here.
