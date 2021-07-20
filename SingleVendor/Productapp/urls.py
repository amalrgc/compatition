
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('',views.Main,name='main'),
    path('create-branch',CreateBranch.as_view()),
    path('patch-branch/<str:pk>',PatchBranch.as_view()),
    path('delete-branch/<str:pk>',PatchBranch.as_view()),
    path('list-branch',ListBranch.as_view()),

    path('create-Product',CreateProduct.as_view()),
    path('patch-Product/<str:pk>',PatchProduct.as_view()),
    path('delete-Product/<str:pk>',PatchProduct.as_view()),
    path('list-Product',ListProduct.as_view()),
   

    path('create-Variant',CreateVariant.as_view()),
    path('patch-Variant/<str:pk>',PatchVariant.as_view()),
    path('delete-Variant/<str:pk>',PatchVariant.as_view()),
    path('list-Variant',ListVariant.as_view()),
   
   
    path('create-Warranty',CreateWarranty.as_view()),
    path('patch-Warranty/<str:pk>',PatchWarranty.as_view()),
    path('delete-Warranty/<str:pk>',PatchWarranty.as_view()),
    path('list-Warranty',ListWarranty.as_view()),


    path('create-CartItems',CreateCartItems.as_view()),
    path('patch-CartItems/<str:pk>',PatchCartItems.as_view()),
    path('delete-CartItems/<str:pk>',PatchCartItems.as_view()),
    path('list-CartItems',ListCartItems.as_view()),
   
    path('create-Orders',CreateOrders.as_view()),
    path('patch-Orders/<str:pk>',PatchOrders.as_view()),
    path('delete-Orders/<str:pk>',PatchOrders.as_view()),
    path('list-Orders',ListOrders.as_view()),
   
    path('create-Profile',CreateProfile.as_view()),
    path('patch-Profile/<str:pk>',PatchProfile.as_view()),
    path('delete-Profile/<str:pk>',PatchProfile.as_view()),
    path('list-Profile',ListProfile.as_view()),
    
    path('create-Checkout',CreateCheckout.as_view()),
    path('patch-Checkout/<str:pk>',PatchCheckout.as_view()),
    path('delete-Checkout/<str:pk>',PatchCheckout.as_view()),
    path('list-Checkout',ListCheckout.as_view()),
    path('ProductSearch',ProductSearch.as_view()),
    path('ProductSort',ProductSort.as_view()),

    path('create-Branch',CreateBranch.as_view()),
    path('patch-Branch/<str:pk>',PatchBranch.as_view()),
    path('delete-Branch/<str:pk>',PatchBranch.as_view()),
    path('list-Branch',ListBranch.as_view()),

   
      

     
    path('Category',views.CategoryList.as_view(),name='Category'),
    path('order-filter',views.OrderFilter.as_view(),name='order-filter'),
    path('request-forgot-password', views.RequestPasswordResetEmail.as_view(), name="request-reset-password"),
    path('reset-confirm/<uidb64>/<token>', views.PasswordTokenCheckAPI.as_view(), name="password-reset-confirm"),
    path('reset-complete/verify', views.SetNewPasswordAPI.as_view(), name="'user-password-reset-complete"),
    path('customer-register',views.CustomerRegister.as_view(),name="customer-register"),
    path('customer-login',views.CustomerLogin.as_view(),name="customer-login"),
    path('customer-logout',views.CustomerLogout.as_view(),name="customer-logout"),








]

