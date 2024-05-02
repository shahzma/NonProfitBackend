from rest_framework import viewsets
from .models import Nonprofit, Foundation, EmailRecord
from .serializers import NonprofitSerializer, FoundationSerializer, EmailRecordSerializer
from rest_framework.response import Response
from rest_framework import status

class NonprofitViewSet(viewsets.ModelViewSet):
    queryset = Nonprofit.objects.all()
    serializer_class = NonprofitSerializer

class FoundationViewSet(viewsets.ModelViewSet):
    queryset = Foundation.objects.all()
    serializer_class = FoundationSerializer

class EmailRecordViewSet(viewsets.ModelViewSet):
    queryset = EmailRecord.objects.all()
    serializer_class = EmailRecordSerializer

    def create(self, request, *args, **kwargs):

        nonprofit_id = request.data.get('nonprofit')
        message_template = "Sending money to nonprofit {name} at address {address}"

        try:
            nonprofit = Nonprofit.objects.get(id=nonprofit_id)
        except Nonprofit.DoesNotExist:
            return Response(
                {'error': 'Nonprofit does not exist.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        message = message_template.format(name=nonprofit.name, address=nonprofit.address)


        print(message)

        email_record = EmailRecord.objects.create(
            nonprofit=nonprofit,
            message=message
        )

        serializer = self.get_serializer(email_record)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)