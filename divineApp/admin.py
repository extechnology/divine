from django.contrib import admin
from django.utils.html import format_html
from .models import *


# ==============================
# PRODUCT INLINE (Category → Products)
# ==============================
class ProductInline(admin.TabularInline):
    model = Products
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    inlines = [ProductInline]


# ==============================
# PROJECTS & GALLERY
# ==============================
class ProjectsAndGalleryImagesInline(admin.TabularInline):
    model = ProjectsAndGalleryImages
    extra = 2
    fields = ("image", "image_preview", "title", "is_main_image")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" />', obj.image.url)
        return "-"
    image_preview.short_description = "Preview"


@admin.register(ProjectsAndGallery)
class ProjectsAndGalleryAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    inlines = [ProjectsAndGalleryImagesInline]




# ==============================
# SERVICE CATEGORY IMAGE INLINE
# ==============================
class ServiceCategoryImageInline(admin.TabularInline):
    model = ServiceCategoryImage
    extra = 4
    fields = ("image", "image_preview", "is_main")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" style="border-radius:6px;" />', obj.image.url)
        return "-"
    image_preview.short_description = "Preview"


# ==============================
# SERVICE CATEGORY ADMIN
# ==============================
@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "service", "created_at")  # ✅ fixed
    search_fields = ("name", "service__name")
    list_filter = ("service",)
    inlines = [ServiceCategoryImageInline]


# ==============================
# SERVICE CATEGORY INLINE (inside Service)
# ==============================
# class ServiceCategoryInline(admin.StackedInline):
#     model = ServiceCategory
#     extra = 1
#     show_change_link = True
#     fields = ("name",)  


# ==============================
# SERVICE ADMIN
# ==============================
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)
    # inlines = [ServiceCategoryInline]


# ==============================
# PRODUCTS ADMIN
# ==============================
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "created_at")


# ==============================
# YOUTUBE LINKS
# ==============================
@admin.register(YouTubeLink)
class YouTubeLinkAdmin(admin.ModelAdmin):
    list_display = ("link", "created_at")



@admin.register(DirectorProfile)
class DirectorProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "created_at")


class AboutUsImageInline(admin.TabularInline):
    model = AboutUsImage
    extra = 4
    fields = ("image", "image_preview", "is_main", "order")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" style="border-radius:6px;" />', obj.image.url)
        return "-"
    image_preview.short_description = "Preview"


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    inlines = [AboutUsImageInline]

@admin.register(AboutUsContents)
class AboutUsContentsAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")

@admin.register(HeroCarousel)
class HeroCarouselAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")

@admin.register(HomePageTextAndImage)
class HomePageTextAndImageAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")

@admin.register(BeforeAndAfter)
class BeforeAndAfterAdmin(admin.ModelAdmin):
    list_display = ("created_at",)

@admin.register(DedicatedServices)
class DedicatedServicesAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")

@admin.register(ProjectInsights)
class ProjectInsightsAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")


# ==============================
# BANNERS
# ==============================
@admin.register(BannerImages)
class BannerImagesAdmin(admin.ModelAdmin):
    list_display = ("banner_type", "created_at")


# ==============================
# CONTACT US
# ==============================
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "created_at")
    readonly_fields = ("name", "email", "phone", "subject", "message", "created_at")

    def has_add_permission(self, request):
        return False  # ❌ prevent manual add

    def has_delete_permission(self, request, obj=None):
        return True  # allow delete if needed