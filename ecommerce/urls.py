"""

Developed By : vernonthedev
Github: github.com/vernonthedev

"""
from django.contrib import admin
from django.urls import path
from ecom import views
from ecom.views import CustomLoginView
from django.contrib.auth.views import LoginView,LogoutView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='ecom/home.html'),name='logout'),
    path('shop', views.shop_view, name='shop'),
    path('aboutus', views.aboutus_view, name='aboutus'),
    path('contactus', views.contactus_view,name='contactus'),
    path('search', views.search_view,name='search'),
    path('send-feedback', views.send_feedback_view,name='send-feedback'),
    path('shipping-policy', views.shipping_policy_view, name='shipping-policy'),
    path('privacy-policy', views.privacy_policy_view, name='privacy-policy'),
    path('terms-and-conditions', views.terms_and_conditions_view, name='terms-and-conditions'),


    ######################### ADMIN URLS
    path('adminclick', views.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='adminDashboard/adminlogin.html'),name='adminlogin'),
    path('admindashboard', views.admin_dashboard,name='admin-dash'),

    path('view-orders', views.admin_view_orders,name='view-orders'),
    path('view-customer', views.view_customer_view,name='view-customer'),
    path('view-feedback', views.view_feedback_view,name='view-feedback'),


    path('delete-customer/<int:pk>', views.delete_customer_view,name='delete-customer'),
    path('update-customer/<int:pk>', views.update_customer_view,name='update-customer'),

    path('admin-products', views.admin_products_view,name='admin-products'),
    path('admin-add-product', views.admin_add_product_view,name='admin-add-product'),
    
    path('delete-product/<int:pk>', views.delete_product_view,name='delete-product'),
    path('update-product/<int:pk>', views.update_product_view,name='update-product'),

    path('admin-view-booking', views.admin_view_booking_view,name='admin-view-booking'),
    path('delete-order/<int:pk>', views.delete_order_view,name='delete-order'),
    path('update-order/<int:pk>', views.update_order_view,name='update-order'),
    #################################################

    path('customersignup', views.customer_signup_view, name="customersignup"),
    # path('customerlogin', LoginView.as_view(template_name='ecom/customerlogin.html'),name='customerlogin'),
    path('customerlogin/', CustomLoginView.as_view(), name='customerlogin'),
    path('customer-home', views.customer_home_view,name='customer-home'),
    path('all-products/<int:product_id>/', views.view_product, name='selected_product'),

    path('my-order', views.my_order_view,name='my-order'),
    path('my-profile', views.my_profile_view,name='my-profile'),
    path('edit-profile', views.edit_profile_view,name='edit-profile'),
    path('download-invoice/<int:orderID>/<int:productID>', views.download_invoice_view,name='download-invoice'),


    path('add-to-cart/<int:pk>', views.add_to_cart_view,name='add-to-cart'),
    path('cart', views.cart_view,name='cart'),
    path('remove-from-cart/<int:pk>', views.remove_from_cart_view,name='remove-from-cart'),
    path('customer-address', views.customer_address_view,name='customer-address'),
    path('payment-success', views.payment_success_view,name='payment-success'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)