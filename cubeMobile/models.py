from django.db import models
from ckeditor.fields import RichTextField

MOBILE = 'mobile'
CLOUD = 'cloud'
WEB = 'website'
DESKTOP = 'desktop'
TYPE_PORTOFLIO_CHOICES = (
    (MOBILE, 'mobile'),
    (CLOUD, 'cloud'),
    (WEB, 'website'),
    (DESKTOP, 'desktop'),
)


class Testimonianl(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='testimonianl/%Y/%m/%d/', blank=False, null=False)
    content = models.CharField(max_length=400, blank=False, null=False)


class Cubian(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='cubians/%Y/%m/%d/', blank=False, null=False)
    content = models.CharField(max_length=400, blank=True, null=True)


class Portoflio(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='portoflio/%Y/%m/%d/', blank=False, null=False)
    description = models.CharField(max_length=400, blank=False, null=False)
    ios_url = models.URLField(max_length=200, default=None, null=True, blank=True)
    android_url = models.URLField(max_length=200, default=None, null=True, blank=True)
    web_url = models.URLField(max_length=200, default=None, null=True, blank=True)
    type = models.CharField(choices=TYPE_PORTOFLIO_CHOICES, max_length=50, null=False, blank=False)


class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=False, null=False)
    description = models.CharField(max_length=400, blank=False, null=False)
    ios_url = models.URLField(max_length=200, default=None, null=True, blank=True)
    android_url = models.URLField(max_length=200, default=None, null=True, blank=True)
    web_url = models.URLField(max_length=200, default=None, null=True, blank=True)


class Certificate(models.Model):
    image = models.ImageField(upload_to='certificates/%Y/%m/%d/', blank=False, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    certificate_url = models.URLField(max_length=200, default=None, null=True, blank=True)
    content = models.CharField(max_length=400, blank=False, null=False)


class Technology(models.Model):
    image = models.ImageField(upload_to='technologies/%Y/%m/%d/', blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    subname = models.CharField(max_length=100, blank=False, null=False)


class Post(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to="posts/%Y/%m/%d/", blank=False, null=False)
    content = RichTextField(('content of post'))
    date = models.DateField(auto_now_add=True)
