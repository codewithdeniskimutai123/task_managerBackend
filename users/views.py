from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.
@api_view(['POST'])

@parser_classes([MultiPartParser, FormParser])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
