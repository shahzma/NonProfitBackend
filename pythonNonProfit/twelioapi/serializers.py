from rest_framework import serializers
from .models import Nonprofit, Foundation, EmailRecord

class NonprofitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nonprofit
        fields = '__all__'

class FoundationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foundation
        fields = '__all__'

class EmailRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailRecord
        fields = '__all__'
