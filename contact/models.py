from django.db import models


class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100, blank=False, null=False)
    phone_no = models.CharField(max_length=20, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    message = models.TextField(blank=False, null=False)


class CV(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    cv = models.FileField(upload_to="CVs/%Y/%m/%d/", blank=False, null=False)
    phone_no = models.CharField(max_length=100, blank=False, null=False)
