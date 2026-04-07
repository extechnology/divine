from divineApp.models import ServiceCategoryImage
from rest_framework import viewsets
from .models import *
from .serializers import *

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class ProjectsAndGalleryViewSet(viewsets.ModelViewSet):
    queryset = ProjectsAndGallery.objects.all()
    serializer_class = ProjectsAndGallerySerializer

class ProjectsAndGalleryImagesViewSet(viewsets.ModelViewSet):
    queryset = ProjectsAndGalleryImages.objects.all()
    serializer_class = ProjectsAndGalleryImagesSerializer

class YouTubeLinkViewSet(viewsets.ModelViewSet):
    queryset = YouTubeLink.objects.all()
    serializer_class = YouTubeLinkSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer


class DirectorProfileViewSet(viewsets.ModelViewSet):
    queryset = DirectorProfile.objects.all()
    serializer_class = DirectorProfileSerializer

class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class AboutUsContentsViewSet(viewsets.ModelViewSet):
    queryset = AboutUsContents.objects.all()
    serializer_class = AboutUsContentsSerializer

class HeroCarouselViewSet(viewsets.ModelViewSet):
    queryset = HeroCarousel.objects.all()
    serializer_class = HeroCarouselSerializer

class HomePageTextAndImageViewSet(viewsets.ModelViewSet):
    queryset = HomePageTextAndImage.objects.all()
    serializer_class = HomePageTextAndImageSerializer

class BeforeAndAfterViewSet(viewsets.ModelViewSet):
    queryset = BeforeAndAfter.objects.all()
    serializer_class = BeforeAndAfterSerializer

class DedicatedServicesViewSet(viewsets.ModelViewSet):
    queryset = DedicatedServices.objects.all()
    serializer_class = DedicatedServicesSerializer

class ProjectInsightsViewSet(viewsets.ModelViewSet):
    queryset = ProjectInsights.objects.all()
    serializer_class = ProjectInsightsSerializer


class BannerImageViewSet(viewsets.ModelViewSet):
    queryset = BannerImages.objects.all()
    serializer_class = BannerImagesSerializer

class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
