from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from . import models
from .models import Customer, Product, Category, SubCategory, Image


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        label='',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        label='',
    )

class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['address', 'mobile', 'profile_pic']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile'}),
            'profile_pic': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
class ProductForm(forms.ModelForm):
    # Define a MultipleChoiceField for the images
    images = forms.ModelMultipleChoiceField(
        queryset=Image.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False  # Set to False to allow no selection
    )

    class Meta:
        model = Product
        fields = ['name', 'category', 'subcategory', 'featured', 'deal_of_the_day', 'best_seller', 'new_arrival', 'trending', 'top_rated', 'inventory', 'number_in_stock', 'price', 'short_description', 'long_description', 'images']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'subcategory': forms.Select(attrs={'class': 'form-control'}),
            'featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'deal_of_the_day': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'best_seller': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'new_arrival': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'trending': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'top_rated': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'inventory': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Inventory'}),
            'number_in_stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number in Stock'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Short Description'}),
            'long_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Long Description'}),
            'images': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),  # Update widget for image
        }

#address of shipment
class AddressForm(forms.Form):
    Email = forms.EmailField()
    Mobile= forms.IntegerField()
    Address = forms.CharField(max_length=500)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=models.Feedback
        fields=['name','feedback']

#for updating status of order
class OrderForm(forms.ModelForm):
    class Meta:
        model=models.Orders
        fields=['status']

#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
