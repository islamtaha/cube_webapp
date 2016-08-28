from django.views import generic
from cubeMobile.models import Testimonianl, Cubian, Portoflio, Product, Post
import django_filters


class IndexView(generic.ListView):
    model = Testimonianl
    context_object_name = 'items'
    template_name = 'index.html'

    def get_queryset(self):
        return Testimonianl.objects.all()


class ProductView(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'projects.html'

    def get_queryset(self):
        return Product.objects.all()


class PortoflioFilter(django_filters.FilterSet):
    class Meta:
        model = Portoflio
        fields = ['type']


class PortoflioView(generic.ListView):
    model = Portoflio
    context_object_name = 'portoflio'
    template_name = 'our_portfolio.html'
    queryset = Portoflio.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        return PortoflioFilter(self.request.GET, queryset)


class AboutView(generic.ListView):
    model = Cubian
    context_object_name = 'workers'
    template_name = 'about_us.html'

    def get_queryset(self):
        return Cubian.objects.all()


class BlogView(generic.ListView):
    template_name = 'Blog.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()


class PostDetailView(generic.DetailView):
    template_name = 'post.html'
    model = Post
