from .models import Training
from rest_framework import serializers


class TrainingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Training
        fields = ('athlete', 'distance', 'current_distance', 'current_lang', 'current_long',
                  'current_alt', 'current_lang')
