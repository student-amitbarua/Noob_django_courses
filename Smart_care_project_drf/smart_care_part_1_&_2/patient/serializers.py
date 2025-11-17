from rest_framework import serializers
from . import models


class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False) # ek model theke arek model er data collect kore show kora 
    class Meta:
        model = models.Patient
        fields = '__all__'