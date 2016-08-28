from cubeMobile.models import Testimonianl, Cubian, Portoflio, Product, Certificate, Technology
from cubeMobile.serializers import TestimonianlSerializer, CubianSerializer
from cubeMobile.serializers import PortoflioSerializer, ProductSerializer
from cubeMobile.serializers import CertificateSerializer, TechnologySerializer
from rest_framework import generics


class TestimonianlAPIList(generics.ListAPIView):
    queryset = Testimonianl.objects.all()
    serializer_class = TestimonianlSerializer


class CubianAPIList(generics.ListAPIView):
    queryset = Cubian.objects.all()
    serializer_class = CubianSerializer


class PortoflioAPIList(generics.ListAPIView):
    queryset = Portoflio.objects.all()
    serializer_class = PortoflioSerializer


class ProductAPIList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CertificateAPIList(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class TechnologyAPIList(generics.ListAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
