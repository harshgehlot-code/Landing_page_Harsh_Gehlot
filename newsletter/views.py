from rest_framework import generics, status
from rest_framework.response import Response
from .models import Subscriber
from .serializers import SubscriberSerializer


class NewsletterSubscribeView(generics.CreateAPIView):
    """
    POST /api/newsletter/
    Creates a new newsletter subscription
    """
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                'message': 'Successfully subscribed to newsletter.',
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )
