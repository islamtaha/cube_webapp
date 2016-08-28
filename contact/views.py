from contact.forms import ContactUsForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic.edit import BaseCreateView
from contact.models import ContactMessage
from django.views import generic


class ContactMessageView(SuccessMessageMixin, generic.CreateView):
    template_name = 'contact.html'
    model = ContactMessage
    form_class = ContactUsForm
    success_url = '/contact_us/'

    def post(self, request, *args, **kwargs):
        self.object = None
        messages.success(request, 'thanks for your message!')
        messages.error(request, 'you are missing some data!')
        return super(BaseCreateView, self).post(request, *args, **kwargs)
