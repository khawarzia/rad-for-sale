from django.db import models
from users.models import User

class Auction(models.Model):
    FAILED = 0
    SUCCESS = 1
    AUCTION_STATUS = (
        (FAILED, 'Failed'),
        (SUCCESS, 'Success')
    )
    seller = models.ForeignKey(User, on_delete=models.PROTECT, related_name="auction_seller")
    buyer = models.ForeignKey(User, on_delete=models.PROTECT, related_name="auction_buyer")
    #listing = models.ForeignKey("listing.Listing", on_delete=models.PROTECT)
    #bid = models.ForeignKey(BidOnListing, on_delete=models.PROTECT)
    buyer_amount_percentage = models.FloatField(default=0.0)
    seller_amount_percentage = models.FloatField(default=0.0)
    status = models.PositiveIntegerField(choices=AUCTION_STATUS, default=SUCCESS)
    # Timestamp
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

