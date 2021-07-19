from django.shortcuts import render,redirect
from .models import*
from .serializer import *
from .utils import *
from django.http import HttpResponse
from . forms import UserRegistrationForm,UserLoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import BranchSerializer
from rest_framework import generics
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import login,logout
from rest_framework.permissions import IsAuthenticated 
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
import uuid
from datetime import date
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text, smart_str, DjangoUnicodeDecodeError,smart_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework import  status,generics
from django.db.models import Q


@api_view(['GET'])
def Main(request):
    api_urls ={
        'customer-register':'/customer-register/',
        'customer-login':'/customer-login/',
        'customer-logout':'/customer-logout/',
        'forgetpassword':'/request-forgot-password/',

         'CreateBranch':'/create-branch/',
         'BranchUpdate':'/patch-branch/',
         'DeleteBranch':'/delete-branch/',
         'ListBranch':'/list-branch/',


          'CreateProduct':'/create-Product/',
         'UpdateProduct':'/patch-Product/',
         'DeleteProduct':'/delete-Product/',
         'ListProduct':'/list-Product/',

         
          'CreateVariant':'/create-Variant/',
         'UpdateVariant':'/patch-Variant/',
         'DeleteVariant':'/delete-Variant/',
         'ListVariant':'/list-Variant/',

          
          'CreateWarranty':'/create-Warranty/',
         'UpdateWarranty':'/patch-Warranty/',
         'DeleteWarranty':'/delete-Warranty/',
         'ListWarranty':'/list-Warranty/',

         'CreateCartItems':'/create-CartItems/',
         'UpdateCartItems':'/patch-CartItems/',
         'DeleteCartItems':'/delete-CartItems/',
         'ListCartItems':'/list-CartItems/',

         'CreateOrders':'/create-Orders/',
         'UpdateOrders':'/patch-Orders/',
         'DeleteOrders':'/delete-Orders/',
         'ListOrders':'/list-Orders/',

         'CreateProfile':'/create-Profile/',
         'UpdateProfile':'/patch-Profile/',
         'DeleteProfile':'/delete-Profile/',
         'ListProfile':'/list-Profile/',

         'CreateCheckout':'/create-Checkout/',
         'UpdateCheckout':'/patch-Checkout/',
         'DeleteCheckout':'/delete-Checkout/',
         'ListCheckout':'/list-Checkout/',

         'CategoryList':'/Category/',
         'ProductSearch':'/ProductSearch/',
        'ProductSort':'/ProductSort/',


        }
    return Response(api_urls)


##PRODUCT SEARCH######################################################################################

class ProductSearch(ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        queryset_list=Products.objects.all()
        query=self.request.GET.get("q")
        if query:
            queryset_list=queryset_list.filter(
                Q(name__icontains=query)
            ).distinct()
        return queryset_list




class ProductSort(APIView):
    def get(self,request):
        sort=request.GET.get("sort")
        var=Variant.objects.all()
        if sort=='asc':
            var=var.order_by('price')
        elif sort=='desc':
            var=var.order_by('-price')
            print("ACS:",var)

        serializer_class = VarientSerializer(var,many=True)
   
        return Response(serializer_class.data)

##Branch START######################################################################################


class CreateBranch(generics.CreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

# class to list files
class ListBranch(generics.ListAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()


# can perform get, patch and delete here
class PatchBranch(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()



##PRODUCT START######################################################################################

class CreateProduct(generics.CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

# class to list files
class ListProduct(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()


# can perform get, patch and delete here
class PatchProduct(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()

##VARIENT START######################################################################################

class CreateVariant(generics.CreateAPIView):
    queryset = Variant.objects.all()
    serializer_class = VarientSerializer

# class to list files
class ListVariant(generics.ListAPIView):
    serializer_class = VarientSerializer
    queryset = Variant.objects.all()


# can perform get, patch and delete here
class PatchVariant(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VarientSerializer
    queryset = Variant.objects.all()
    




##WRRANTY START######################################################################################

class CreateWarranty(generics.CreateAPIView):
    queryset = Warranty.objects.all()
    serializer_class = WarrantySerializer

# class to list files
class ListWarranty(generics.ListAPIView):
    serializer_class = WarrantySerializer
    queryset = Warranty.objects.all()


# can perform get, patch and delete here
class PatchWarranty(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WarrantySerializer
    queryset = Warranty.objects.all()
    




##CART START######################################################################################


class CreateCartItems(generics.CreateAPIView):
    queryset = CartItems.objects.all()
    serializer_class = CartSerializer

# class to list files
class ListCartItems(generics.ListAPIView):
    serializer_class = CartSerializer
    queryset = CartItems.objects.all()


# can perform get, patch and delete here
class PatchCartItems(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    queryset = CartItems.objects.all()
    




##ORDER START######################################################################################


class CreateOrders(generics.CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

# class to list files
class ListOrders(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Orders.objects.all()


# can perform get, patch and delete here
class PatchOrders(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Orders.objects.all()








##PROFILE START######################################################################################


class CreateProfile(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# class to list files
class ListProfile(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


# can perform get, patch and delete here
class PatchProfile(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()



##CHECKOUT START######################################################################################



class CreateCheckout(generics.CreateAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

# class to list files
class ListCheckout(generics.ListAPIView):
    serializer_class = CheckoutSerializer
    queryset = Checkout.objects.all()


# can perform get, patch and delete here
class PatchCheckout(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CheckoutSerializer
    queryset = Checkout.objects.all()





# @api_view(['GET'])
# @permission_classes((IsAuthenticated, ))

# def BranchList(request):
#     branchs=Branch.objects.all()
#     serializer=BranchSerializer(branchs,many=True)
#     return Response(serializer.data)


class OrderFilter(APIView):
    def get(self,request):
        today = today = date.today()
        orders = Orders.objects.filter(order_date=today)
        order_serilaizer = OrderSerializer(orders,many=True)
        return Response({"status":"success","data":order_serilaizer.data})
    def post(self, request):
        from_date = request.data['from']
        to_date = request.data['to']
        orders = Orders.objects.filter(order_date__range=[from_date,to_date])
        if orders:
            order_serializer = OrderSerializer(orders,many=True)
            return Response({"status":"success","data":order_serializer.data})
        else:
            return Response({"status":"failed","message":"no orders in this dates"})
        



class CategoryList(ListAPIView):
    model = Category
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(level=0)


class CustomerRegister(APIView):    
    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerLogin(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                'message': 'You have successfully Logged in.',
                'user': user.id,
                'token': token.key
            },
            status=status.HTTP_200_OK)

class CustomerLogout(APIView):
    permission_classes = (IsAuthenticated,) 
    def get(self, request, format=None):
        logout(request)
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        email = request.data['email']
        
        if not MyUser.objects.filter(email=email).exists():
            return Response({"status":"invalid user"})
        else:
            user = MyUser.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(request=request).domain
            relativeLink = reverse('password-reset-confirm',kwargs={'uidb64':uidb64, 'token':token})
            absurl = 'http://'+current_site+relativeLink
            email_body = 'Hello \n Use below link to reset your password \n '+absurl 
            data = {'email_body':email_body, 'to_email':user.email,'email_subject':'Reset your password'}

            Util.send_email(data)
            return Response({"status":"success","data":"email sent"})

class PasswordTokenCheckAPI(generics.GenericAPIView):
    def get(self, request, uidb64, token):
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = MyUser.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': 'Token is not valid, Please request a new one'})
            
            return Response({'success':True, 'message':'credantials valid', 'uidb64':uidb64, 'token':token})
        except DjangoUnicodeDecodeError as identifier:
            return Response({'error': 'Token is not valid, please request a new one'}, status=status.HTTP_400_BAD_REQUEST)

class SetNewPasswordAPI(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success':True, 'message':'password reset success','data':serializer.data})

