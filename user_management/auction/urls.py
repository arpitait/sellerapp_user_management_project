from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("auction",views.AuctionView)
router.register("bid",views.BidView)


urlpatterns = [
    path("ongoing_auction/",views.OngoingAuctionView.as_view({'get': 'list'}),name="ongoing-auctions"),
    path("api/",include(router.urls)),
]
