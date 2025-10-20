from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import CustomUserSerializer, UserProfileSerializer
from rest_framework.generics import CreateAPIView

# Create your views here.
@api_view(['GET','POST'])
def register(request):
    serializer_item = CustomUserSerializer(data=request.data)
    serializer_item.is_valid(raise_exception=True)
    serializer_item.save()
    return Response(serializer_item.validated_data,status.HTTP_201_CREATED)

class RegisterView(CreateAPIView):
    serializer_class = CustomUserSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = 