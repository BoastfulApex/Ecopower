from rest_framework.generics import ListAPIView
from .serializers import BrandSerializer, CarSerializer, VideoSerializer, AboutSerializer, ImageSerializer, FAQSerializer
from .models import Brand, Car, Video, About, Image, FAQ

class BrandListView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class CarListView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class VideoListView(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class AboutListView(ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class ImageView(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class FAQListView(ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

class TopCarsAPIView(ListAPIView):
    queryset = Car.objects.filter(top=True)
    serializer_class = CarSerializer