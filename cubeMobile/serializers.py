from rest_framework import serializers
from cubeMobile.models import Testimonianl, Cubian, Portoflio, Product, Certificate, Technology


class TestimonianlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonianl
        fields = ['name', 'title', 'image', 'content']


class CubianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cubian
        fields = ['name', 'title', 'image', 'content']


class PortoflioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portoflio
        fields = ['name', 'description', 'image', 'android_url', 'web_url', 'ios_url', 'type']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'ios_url', 'android_url', 'web_url']


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['certificate_url', 'title', 'image', 'content']


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['name', 'subname', 'image']
