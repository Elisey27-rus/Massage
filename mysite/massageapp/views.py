from django.http import HttpResponse
import pymysql
from rest_framework import viewsets
from .models import EmailAccount, EmailMessage
from .serializers import EmailAccountSerializer, EmailMessageSerializer
from passwords import host, port, user, password, database


def test(request):
    try:
        connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
        )
        connection.close()
        return HttpResponse("Good connection")
    except Exception as ex:
        print(ex)
        return HttpResponse(f"Error connecting to database: {str(ex)}")


class EmailAccountViewSet(viewsets.ModelViewSet):
    queryset = EmailAccount.objects.all()
    serializer_class = EmailAccountSerializer


class EmailMessageViewSet(viewsets.ModelViewSet):
    queryset = EmailMessage.objects.all()
    serializer_class = EmailMessageSerializer
