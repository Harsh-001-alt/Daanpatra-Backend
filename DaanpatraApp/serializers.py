from django.contrib.auth.models import Permission
from rest_framework import serializers
from . models import *
from oauth2_provider.models import AccessToken
from django.core.exceptions import PermissionDenied
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from rest_framework.response import Response
from django.conf import settings

class FilteredUserSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        if self.context['request'].user.has_perm('DaanpatraApp.view_user'):
            data = User.objects.all()
            return super(FilteredUserSerializer, self).to_representation(data)
        else:
            raise PermissionDenied()

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    birth_date = serializers.CharField(required=True)

    class Meta:
        list_serializer_class = FilteredUserSerializer     
        model = User
        fields = "__all__"

    def create(self,validated_data):
        user =  self.context['request'].user
        role = validated_data.get('role')
        if role == 'Sub_Admin':
            if user.has_perm('DaanpatraApp.can_add_sub_admin'):
                user = User.objects.create(
                    email = validated_data.get('email'),
                    username = validated_data.get('username'),
                    password = validated_data.get('password'),
                    name = validated_data.get('name'),
                    birth_date = validated_data.get('birth_date'),
                    role=role
                )
                user.set_password(validated_data.get('password'))
                user.save()
                return user
            else:
                raise PermissionDenied()
        else:
            user = User.objects.create(
                email = validated_data.get('email'),
                username = validated_data.get('username'),
                password = validated_data.get('password'),
                name = validated_data.get('name'),
                birth_date = validated_data.get('birth_date'),
            )
            user.set_password(validated_data.get('password'))
            user.save()
            return user


        # if user.has_perm('DaanpatraApp.can_add_drivers'):
        #     user = User.objects.create(
        #         email = validated_data.get('email'),
        #         username = validated_data.get('username'),
        #         password = validated_data.get('password'),
        #         name = validated_data.get('name'),
        #         birth_date = validated_data.get('birth_date'),
        #     )
        #     user.set_password(validated_data.get('password'))
        #     delete_perm = Permission.objects.get(codename='delete_user')
        #     view_perm = Permission.objects.get(codename='view_user')
        #     update_perm = Permission.objects.get(codename='change_user')
        #     user.user_permissions.add(view_perm, update_perm, delete_perm)
        #     user.save()
        #     return user
        # else:
        #     raise PermissionDenied()


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class DriverActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user.has_perm('DaanpatraApp.can_update_drivers'):
            instance.name = validated_data.get('name', instance.name)
            instance.username = validated_data.get('username', instance.username)
            instance.email = validated_data.get('email', instance.email)
            instance.birth_date = validated_data.get('birth_date', instance.birth_date)
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.birth_date = validated_data.get('birth_date', instance.birth_date)
            instance.role = validated_data.get('role', instance.role)
            instance.save()
            if validated_data.get('password'):
                instance.set_password(validated_data.get('password'))
                instance.save()
            return instance
        else:
            raise PermissionDenied()


class UserActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user.has_perm('DaanpatraApp.change_user'):
            instance.name = validated_data.get('name', instance.name)
            instance.username = validated_data.get('username', instance.username)
            instance.email = validated_data.get('email', instance.email)
            instance.birth_date = validated_data.get('birth_date', instance.birth_date)
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.birth_date = validated_data.get('birth_date', instance.birth_date)
            instance.role = validated_data.get('role', instance.role)
            instance.save()
            if validated_data.get('password'):
                instance.set_password(validated_data.get('password'))
                instance.save()
            return instance
        else:
            raise PermissionDenied()


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '__all__'


class DonationSerializer(serializers.ModelSerializer):
    Product_Images = ProductImagesSerializer(many=True)
    class Meta:
        model = Donation
        fields = '__all__'
    
    def create(self, validated_data):
        user = self.context['request'].user
        product_images = validated_data.pop('Product_Images')
        obj = Donation.objects.create(user=user, **validated_data)
        for x in product_images:
            ProductImages.objects.create(donation=obj, **x)
        return obj

# class FundDonationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FundDonation
#         fields = '__all__'

#================================================================================
class FilteredDonationSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = Donation.objects.filter(assign_to=self.context['request'].user.uuid)
        return super(FilteredDonationSerializer, self).to_representation(data)


class DonationActionsSerializer(serializers.ModelSerializer):
    Product_Images = ProductImagesSerializer(many=True)
    class Meta:
        list_serializer_class = FilteredDonationSerializer
        model = Donation
        fields = '__all__'
#================================================================================

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'