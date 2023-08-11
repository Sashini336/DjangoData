from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Ads
from .serializers import AdsSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from Ads.serializers import UserSerializer
from django.core.management import call_command

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AdsViewSet(viewsets.ModelViewSet):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer

@api_view(['GET', 'POST'])  
def add_url(request):
    if request.method == 'GET':
        ads = Ads.objects.all()  
        serializer = AdsSerializer(ads, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        url = data.get("data")
        call_command('automoto', url) 
        return Response({"message": "Raboti"}) 
