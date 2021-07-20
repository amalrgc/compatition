from django.db.models import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from rest_framework_recursive.fields import RecursiveField

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class VarientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = "__all__"

class WarrantySerializer(serializers.ModelSerializer):
    class Meta:
        model = Warranty
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = "__all__"




class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = "__all__"




class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"




class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"



class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


# class CategorySerializer(serializers.ModelSerializer):
#      children = serializers.ListField(
#         read_only=True, source='your_get_children_method', child=RecursiveField()) 
#      class Meta:
#         model = Category
#         fields = "__all__"
#         # children = serializers.ListField(
#         # read_only=True, source='your_get_children_method', child=RecursiveField()
    


class CategorySerializer(serializers.ModelSerializer):
    leaf_nodes = serializers.SerializerMethodField()

    class Meta:
        depth = 1
        model = Category
        fields = "__all__"

    def get_leaf_nodes(self, obj):
        return CategorySerializer(obj.get_children(), many=True).data


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('email', 'name', 'phone', 'password','username')

        def create(self, validated_data):
            user = MyUser(
                name=validated_data['name'],
                email=validated_data['email'],
                phone=validated_data['phone'],
                username=validated_data['username']
                )
            user.set_password(validated_data['password'])
            user.is_active = False
            user.is_staff = True
            user.save()
            return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers .CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        obj = MyUser.objects.get(email=email)
    
        if obj.is_active == True:
            user = MyUser.objects.get(password=password)
            print(user)
            if user:
                data['user'] = user
            else:
                msg = 'login failed'
                raise exceptions.ValidationError(msg)
        return data

class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    class Meta:
        fields = ['user_email']


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=5, max_length=20, write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        fields = ['password','token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = MyUser.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid')
            user.set_password(password)
            user.show_password = password
            user.save()

            return(user)
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid')
        return super().validate(attrs)