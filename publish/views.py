from django.shortcuts import render
from .models import Training
from rest_framework import viewsets
from publish.serializers import TrainingSerializer
# Create your views here.


def home(request):
    training = Training.objects.first()
    return render(request, 'publish/home.html', {'training':training})


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
