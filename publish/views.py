from django.shortcuts import render
from .models import Training
# Create your views here.


def home(request):
    training = Training.objects.first()
    return render(request, 'publish/home.html', {'training':training})
