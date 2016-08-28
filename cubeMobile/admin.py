from django.contrib import admin

from cubeMobile.models import Testimonianl, Cubian, Portoflio, Product, Certificate, Technology
from cubeMobile.models import Post


class TestimonianlAdmin(admin.ModelAdmin):
    fields = ['name', 'title', 'image', 'content']
    list_display = ['name', 'title', 'image', 'content']


class CubianAdmin(admin.ModelAdmin):
    fields = ['name', 'title', 'image', 'content']
    list_display = ['name', 'title', 'image', 'content']


class PortoflioAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'image', 'android_url', 'web_url', 'ios_url', 'type']
    list_display = ['name', 'description', 'image', 'android_url', 'web_url', 'ios_url', 'type']


class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'image', 'ios_url', 'android_url', 'web_url']
    list_display = ['name', 'description', 'image', 'ios_url', 'android_url', 'web_url']


class CertificateAdmin(admin.ModelAdmin):
    fields = ['certificate_url', 'title', 'image', 'content']
    list_display = ['certificate_url', 'title', 'image', 'content']


class TechnologyAdmin(admin.ModelAdmin):
    fields = ['name', 'subname', 'image']
    list_display = ['name', 'subname', 'image']


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'image', 'content']
    list_display = ['title', 'image', 'content']


admin.site.register(Testimonianl, TestimonianlAdmin)
admin.site.register(Cubian, CubianAdmin)
admin.site.register(Portoflio, PortoflioAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Post, PostAdmin)
