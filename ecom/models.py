from django.db import models
from django.contrib.auth.models import User
import uuid
import os



class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Image(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='product_images/', null=True, blank=True, max_length=255)

    def __str__(self):
        return f"Image for {self.product.name}"

def get_image_upload_path(instance, filename):
    # Generate a unique folder path for each product
    product_folder = f"product_{instance.product.id}"
    return os.path.join(product_folder, filename)

class Product(models.Model):
    name = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    featured = models.BooleanField(default=False)
    deal_of_the_day = models.BooleanField(default=False)
    best_seller = models.BooleanField(default=False)
    new_arrival = models.BooleanField(default=False)
    trending = models.BooleanField(default=False)
    top_rated = models.BooleanField(default=False)
    inventory = models.PositiveIntegerField(default=0)
    number_in_stock = models.PositiveIntegerField(default=0)
    selling_price = models.PositiveIntegerField(default=0)
    discount_price = models.PositiveIntegerField(default=0)
    short_description = models.CharField(max_length=40, default="")
    long_description = models.TextField(max_length=1000, default="")
    images = models.ManyToManyField(Image, blank=True, related_name='product_images')

    def __str__(self):
        return self.name

# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)

    def __str__(self):
        return f"Order by #{self.customer} is {self.status}"


class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name


# Data model for the subscriptions made through the footer
class Subscriber(models.Model):
    email=models.EmailField(max_length=50,null=True)
    def __str__(self):
        return f"New Subscription from: {self.email}"