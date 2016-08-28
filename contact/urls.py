from django.conf.urls import url
from contact import views
from contact import api_views


urlpatterns = [
    url(r'^api/v1/contact_us/$', api_views.ContactMessageAPICreate.as_view(), name='api_contact_us'),
    url(r'^contact_us/$', views.ContactMessageView.as_view(), name='contact_us'),
]
