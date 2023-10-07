from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Auction,Bid
from .serializers import AuctionSerializer,BidSerializer
from django.utils import timezone


# Create your views here.
class AuctionView(viewsets.ModelViewSet):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()

class OngoingAuctionView(viewsets.ReadOnlyModelViewSet):
    serializer_class = AuctionSerializer

    def get_queryset(self):
        now = timezone.now()
        return Auction.objects.filter(start_time__lte=now, end_time__gt=now)


class BidView(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



