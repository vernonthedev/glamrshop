from django.contrib import admin
from django import forms
from .models import Customer,Product,Orders,Feedback, Image, Category, SubCategory, Subscriber
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
    def __str__(self):
        return f"{self.user}"
admin.site.register(Customer, CustomerAdmin)

class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    def __str__(self):
        return f"{self.name}"
admin.site.register(Category, CategoryAdmin)

class SubCategoryAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"
    def __str__(self):
        return f"{self.name} under {self.category}"
admin.site.register(SubCategory, SubCategoryAdmin)



class ImageInline(admin.TabularInline):
    model = Image
    extra = 3  # Number of empty image slots to display

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'selling_price', 'discount_price','inventory')  # Customize the list display as needed
    list_filter = ('category', 'subcategory', 'featured', 'deal_of_the_day', 'best_seller', 'new_arrival', 'trending', 'top_rated')
    search_fields = ('name', 'description', 'short_description', 'long_description')

    fieldsets = [
        ('Product Information', {'fields': ['name', 'category', 'subcategory', 'selling_price','discount_price']}),
        ('Flags', {'fields': ['featured', 'deal_of_the_day', 'best_seller', 'new_arrival', 'trending', 'top_rated']}),
        ('Stock Information', {'fields': ['inventory', 'number_in_stock']}),
        ('Descriptions', {'fields': ['short_description', 'long_description']}),
    ]

    inlines = [ImageInline]  # Add the ImageInline to the ProductAdmin

admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
    def __str__(self):
        return f"Order #{self.pk}"
admin.site.register(Orders, OrderAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"
    def __str__(self):
        return f"{self.name}"
admin.site.register(Feedback, FeedbackAdmin)

class SubscriberAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"
    def __str__(self):
        return f"{self.email}"
admin.site.register(Subscriber, SubscriberAdmin)