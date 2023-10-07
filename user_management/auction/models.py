from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Auction(models.Model):
    item_name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    start_price = models.DecimalField(max_digits=10,decimal_places=2)
    winner = models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.item_name

class Bid(models.Model):
    auction = models.ForeignKey(Auction,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)


def determine_auction_winner(auction_id):
    auction = Auction.objects.get(pk=auction_id)
    highest_bid = Bid.objects.filter(auction=auction).order_by('-amount').first()
    if highest_bid:
        auction.winner = highest_bid.user
        auction.save()