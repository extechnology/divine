from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = Products
        fields = '__all__'

class ProjectsAndGalleryImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectsAndGalleryImages
        fields = '__all__'

class ProjectsAndGallerySerializer(serializers.ModelSerializer):
    images = ProjectsAndGalleryImagesSerializer(many=True, read_only=True, source='projectsandgalleryimages_set')
    class Meta:
        model = ProjectsAndGallery
        fields = '__all__'


# service sections

class ServiceCategoryImageSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    service_name = serializers.CharField(source='category.service.name', read_only=True)
    
    class Meta:
        model = ServiceCategoryImage
        fields = ["id", "image", "is_main", "category_name", "service_name"]


class ServiceCategorySerializer(serializers.ModelSerializer):
    images = ServiceCategoryImageSerializer(many=True, read_only=True)
    service_name = serializers.CharField(source='service.name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = ServiceCategory
        fields = ["id", "name", "images", "service_name", "category_name"]


class ServiceSerializer(serializers.ModelSerializer):
    categories = ServiceCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = ["id", "name", "categories"]





class DirectorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectorProfile
        fields = '__all__'


class AboutUsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsImage
        fields = ["id", "image", "is_main", "order"]


class AboutUsSerializer(serializers.ModelSerializer):
    images = AboutUsImageSerializer(many=True, read_only=True)
    class Meta:
        model = AboutUs
        fields = '__all__'


class AboutUsContentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsContents
        fields = '__all__'

class HeroCarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroCarousel
        fields = '__all__'

class HomePageTextAndImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePageTextAndImage
        fields = '__all__'

class BeforeAndAfterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeforeAndAfter
        fields = '__all__'

class DedicatedServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DedicatedServices
        fields = '__all__'

class ProjectInsightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectInsights
        fields = '__all__'





class YouTubeLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouTubeLink
        fields = '__all__'

class BannerImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImages
        fields = '__all__'

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'
