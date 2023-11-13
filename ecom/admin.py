from django.contrib import admin
from .models import Customer,Product,Orders,Feedback
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
    def __str__(self):
        return f"{self.user}"
admin.site.register(Customer, CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
    def __str__(self):
        return f"{self.name}"
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
# Register your models here.
