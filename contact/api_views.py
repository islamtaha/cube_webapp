from rest_framework import generics, response, status
from django.core.mail import send_mail
from django.contrib.auth.models import User
from contact.serializers import ContactMessageSerializer
from contact.models import ContactMessage


class ContactMessageAPICreate(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def send_email_to_admin(self, serializer):
        admins_emails = [u.email for u in User.objects.all()]
        customer = serializer.instance
        # Send the customer an email saying that we'be received his request
        send_mail(
            "We received your message!!",
            customer.message,
            'info@app7185521c85a541fd9afdd770b1a64c8a.mailgun.org',
            [customer.email, ]
        )
        # Send the admins an email saying You have a new message from a customer
        for e in admins_emails:
            send_mail(
                "message from contact!!",
                customer.message,
                'info@app7185521c85a541fd9afdd770b1a64c8a.mailgun.org',
                [e, ]
            )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        self.send_email_to_admin(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
