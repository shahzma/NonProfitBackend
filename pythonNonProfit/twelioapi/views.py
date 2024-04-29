from rest_framework import viewsets
from .models import Nonprofit, Foundation, EmailRecord
from .serializers import NonprofitSerializer, FoundationSerializer, EmailRecordSerializer

class NonprofitViewSet(viewsets.ModelViewSet):
    queryset = Nonprofit.objects.all()
    serializer_class = NonprofitSerializer

class FoundationViewSet(viewsets.ModelViewSet):
    queryset = Foundation.objects.all()
    serializer_class = FoundationSerializer

class EmailRecordViewSet(viewsets.ModelViewSet):
    queryset = EmailRecord.objects.all()
    serializer_class = EmailRecordSerializer
