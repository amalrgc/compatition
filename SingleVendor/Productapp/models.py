from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from  mptt.models import MPTTModel , TreeForeignKey

class MyUserManager(BaseUserManager):
    def create_user(self,email,phone,username,password=None):
        if not email:
            raise ValueError("email is required")
        
        if not phone:
            raise ValueError("Please provide active phone number")
        if not username:
            raise ValueError("User name is required")

        user=self.model(
           email=self.normalize_email(email),
           username=username,
           phone=phone,



        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,phone,password=None):
        user=self.create_user(
            email=email,
            username=username,
            
            phone=phone,
            password=password
        )    
        user.is_admin=True
        user.is_superuser=True
        user.save(using=self._db)
        return user




class MyUser(AbstractBaseUser):
    username=models.CharField(verbose_name='user name',max_length=60)
    email=models.EmailField(verbose_name="email address", max_length=60,unique=True)
    name=models.CharField(verbose_name='name',max_length=60,null=True,blank=True)
    phone=models.CharField(verbose_name="Mobile number",max_length=20)
    date_joined=models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_login=models.DateTimeField(verbose_name="last login",auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=True)
    
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username","phone"]
    objects=MyUserManager()
    

    def __str__(self):
        return self.username


    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True 





class Branch(models.Model):
    location = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f'{self.location} location on {self.name} branch '

  
class Category(MPTTModel):
    parent=TreeForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='children')
    name = models.CharField(max_length=100, blank=True, null=True)
    published=models.DateTimeField(auto_now_add=True)
    class MPTTMeta:
      order_insertion_by =['published']
  
    def __str__(self):
        return f'{self.name} '

class Brand(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    description=models.CharField(max_length=100,blank=False,null=False)
    meta=models.JSONField()
    status = models.BooleanField(default=False)
    def __str__(self):
            return f'{self.name} Brand '


class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank= True,null=True)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE,blank= True,null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    product_code = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True, null=True, blank=False)
   
    def __str__(self):
        return f'{self.name} with  {self.product_code}  '




class Variant(models.Model):
    product= models.ForeignKey(Products,on_delete=models.SET_NULL, blank= True,null=True)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE,blank= True,null=True)

    variant_code = models.CharField(max_length=100, blank=True, null=True)

    description = models.TextField(null=True,blank=True)
    price = models.IntegerField(blank=True, null=True)
    image =  models.ImageField(upload_to='images',blank= True,null=True)
    quantity = models.IntegerField(blank=True, null=True)     
                                                                                                                                                                                                                                                                                                  
    def __str__(self):
        return f'{self.variant_code} type  {self.product.name}'


class Warranty(models.Model):
    product= models.ForeignKey(Products,on_delete=models.SET_NULL, blank= False,null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(null=True,blank=True)
      
    def __str__(self):
        return f' Warranty of {self.product.name}  is {self.duration} years'



class CartItems(models.Model):
    variant = models.ForeignKey(Variant,on_delete=models.SET_NULL, blank= False,null=True)
    Customer = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return f'  {self.Customer}  is Added  {self.variant} Products'



  
class Checkout(models.Model):
    Customer = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    products_addedd = models.TextField(null=True,blank=True)
    grand_total = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=100, blank=True, null=True)
    landmark = models.CharField(max_length=100, blank=True, null=True)
   
    def __str__(self):
        return f'  {self.Customer}  is Checkout  {self.products_addedd} Products'



class Orders(models.Model):
    checkout = models.ForeignKey(Checkout, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, default="pending",blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    Customer = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    price = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return f'  {self.Customer}  is Ordered'




class Profile(models.Model):
    Customer = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)