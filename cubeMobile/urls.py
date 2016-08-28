from django.conf.urls import url
from cubeMobile import views
from cubeMobile import api_views


urlpatterns = [
    url(r'^api/v1/testimonianls/$', api_views.TestimonianlAPIList.as_view(), name='api_testimonianls'),
    url(r'^api/v1/cubians/$', api_views.CubianAPIList.as_view(), name='api_cubian'),
    url(r'^api/v1/portoflio/$', api_views.PortoflioAPIList.as_view(), name='api_portoflio'),
    url(r'^api/v1/products/$', api_views.ProductAPIList.as_view(), name='api_product'),
    url(r'^api/v1/certificates/$', api_views.CertificateAPIList.as_view(), name='api_certificate'),
    url(r'^api/v1/technologies/$', api_views.TechnologyAPIList.as_view(), name='api_technology'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^products/$', views.ProductView.as_view(), name='projects'),
    url(r'^portoflio/$', views.PortoflioView.as_view(), name='portoflio'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^blog/$', views.BlogView.as_view(), name='blog'),
    url(r'^blog/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='post'),
]
