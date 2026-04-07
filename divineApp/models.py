from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    brochure = models.FileField(upload_to='brochures',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    warranty = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class ProjectsAndGallery(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProjectsAndGalleryImages(models.Model):
    project = models.ForeignKey(ProjectsAndGallery, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects')
    title = models.CharField(max_length=100)
    is_main_image = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project.title





class Service(models.Model):  # ✅ singular
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ServiceCategory(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="categories"
    )
    name = models.CharField(max_length=100) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service.name} - {self.name}"


class ServiceCategoryImage(models.Model):
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(upload_to='category_images/')
    is_main = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category.name} Image"  # ✅ fixed

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["category"],
                condition=models.Q(is_main=True),
                name="unique_main_image_per_category"
            )
        ]


class YouTubeLink(models.Model):
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link


BANNER_CHOICES = [
    ('about', 'About'),
    ('services', 'Services'),
    ('gallery', 'Gallery'),
    ('contact', 'Contact'),
    ('parallax','Parallax'),
]

class BannerImages(models.Model):
    image = models.ImageField(upload_to='banner')
    banner_type = models.CharField(max_length=100, choices=BANNER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.banner_type


class DirectorProfile(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='director')
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class AboutUsImage(models.Model):
    about = models.ForeignKey(
        AboutUs,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(upload_to='about/')
    is_main = models.BooleanField(default=False)  
    order = models.PositiveIntegerField(default=0)  

    def __str__(self):
        return f"{self.about.title} Image"


class AboutUsContents(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='about')
    sub_title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class HeroCarousel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='hero_carousel')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class HomePageTextAndImage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='home_page_text_and_image')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BeforeAndAfter(models.Model):
    before = models.ImageField(upload_to='before_and_after')
    after = models.ImageField(upload_to='before_and_after')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Before and After {self.id}"


class DedicatedServices(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProjectInsights(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_insights')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name