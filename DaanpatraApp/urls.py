from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from . import views as view
router = DefaultRouter()

router.register(r"register", view.UserViewSet, "register")
router.register(r"driver-actions", view.DriverActionsViewset, "driver_actions")
router.register(r"user-actions", view.UserActionsViewset, "user_actions")
router.register(r"donation", view.DonationViewSet, "donation")
# router.register(r"fund-donation", view.FundDonationViewSet, "fund_donation")
router.register(r"donation-actions", view.DonationActionsViewSet, "donation_actions")
router.register(r"test", view.TestViewSet, "test")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('login/', view.Login.as_view(), name='login'),
] 