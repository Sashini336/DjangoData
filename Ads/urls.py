from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdsViewSet
from .models import Ad
from serializers import AdsSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.urlpatterns import format_suffix_patterns
from Ads import views

router = DefaultRouter()
router.register(r'ads', AdsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('ads', views.ads_list),
    path('ads/<int:id>/', views.ads_detail),
]

urlpattern = format_suffix_patterns(urlpatterns)


@api_view(['GET', 'POST'])
def snippet_list(request):
    
    if request.method == 'GET':
        ads = Ad.objects.all()
        serializer = AdsSerializer(ads, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AdsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
