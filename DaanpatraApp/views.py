"""
-----------------------------------
Steps to create AuthToken Manually.
-----------------------------------
def create(self, request):
    try:
        user = User.objects.get(email=request.data.get('email'), password=request.data.get('password'))
        token = Token.objects.create(user=user)
        return Response({"Token":token.key, "Username":user.name,"Email":user.email})
    except :
        return Response({"Message":"Credentials are incorrect."})
"""
from django.core.exceptions import PermissionDenied
from rest_framework.generics import GenericAPIView 
from django.views.generic.edit import CreateView
from oauth2_provider.models import AccessToken
import requests
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from . models import *
from . serializers import *
from rest_framework.permissions import IsAuthenticated
import json 
from django.conf import settings

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
        
    def retrieve(self, request, pk=None):
        response = {'message': 'Invalid Path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, pk=None):
        response = {'message': 'Invalid Path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, pk=None):
        response = {'message': 'Invalid Path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):
        response = {'message': 'Invalid Path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)



class Login(GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        response = requests.post("http://127.0.0.1:8000/o/token/", 
        data={
            'username':request.data.get('username'),
            'password':request.data.get('password'),
            'grant_type':'password',
            'client_id':settings.CLIENT_ID,
            'client_secret':settings.CLIENT_SECRET

        }
        
        )
        json_data = json.loads(response.text)
        token = json_data.get('access_token')
        token_data = AccessToken.objects.get(token=token)
        user = User.objects.get(uuid=token_data.user.uuid)
        
        user_details = {
            'Username':user.username,
            'Name':user.name,
            'Email':user.email,
            'Birth Date':user.birth_date,
            'Role':user.role,
            'Permissions':user.get_all_permissions(),
            
        }
        return Response({'Data':response.json(),'User':user_details})


class DriverActionsViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = DriverActionsSerializer

    def list(self, request, pk=None):
        response = {'message': 'Invalid Path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, pk=None):
        response = {'message': 'Invalid Path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def post(self, request, pk=None):
        response = {'message': 'Invalid Path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        if request.user.has_perm('DaanpatraApp.can_remove_drivers'):
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({"Message":"User Deleted"})
        else:
            raise PermissionDenied()


class UserActionsViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserActionsSerializer


class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer


class ProductImagesViewSet(viewsets.ModelViewSet):
    queryset = ProductImages.objects.all()
    serializer_class = ProductImagesSerializer

# class FundDonationViewSet(viewsets.ModelViewSet):
#     queryset = FundDonation.objects.all()
#     serializer_class = FundDonationSerializer

#     def create(self, request):
#         user = self.request.user
#         card_no = request.data.get('card_no')
#         exp_month = request.data.get('exp_month')
#         exp_year = request.data.get('exp_year')
#         cvc = request.data.get('cvc')
#         amount = request.data.get('amount')

#         import stripe
#         stripe.api_key = settings.STRIPE_API_KEY
        
#         card = stripe.Token.create(
#             card={
#                 "number": card_no,
#                 "exp_month": exp_month,
#                 "exp_year": exp_year,
#                 "cvc": cvc,
#             },
#         )

#         charge = stripe.Charge.create(
#             amount= int(amount) * 100,
#             currency="inr",
#             description="Donation",
#             source=card.id, # obtained with Stripe.js
#         )

#         import time
#         timestamp = charge.created + 19800
#         ts = time.gmtime(timestamp)
#         date = time.strftime("%Y-%m-%d", ts)
#         time = time.strftime("%H:%M:%S", ts)

#         FundDonation.objects.create(user=user, date=date, time=time, amount=int(amount))
#         if charge.status == 'succeeded':
#             return Response({"Message":"Fund Donated Successfully."})
#         else:
#             return Response({"Message":"Fund Transfer Failed."})

class DonationActionsViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationActionsSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = TestSerializer

    def list(self, request):
        x = print(self.request.user.uuid)
        y = User.objects.filter(uuid=x)
        print(y)
        for x in y:
            print(x.profile)
        from PIL import Image, ImageDraw, ImageFont
        import pandas as pd
        pro = Image.open("/home/harsh/Pictures/test.png") #25x25
        profile = pro.resize((1200,1500))
        name_list = ['Harsh Malviya','Jhonny Depp']
        for i in name_list:
            im = Image.open("/home/harsh/Certificate/Sample.png")
            d = ImageDraw.Draw(im)
            location = (3000, 3000)
            font = ImageFont.truetype("/home/harsh/Certificate/04b_08/04B_08__.TTF", 250)
            d.text(location,i,fill=9,font=font)
            im.paste(profile,(550,700))
            im.save("certificate_"+i+".pdf")

