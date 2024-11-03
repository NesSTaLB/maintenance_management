from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from core.views import (
    home,
    register,
    maintenance_requests,
    MaintenanceRequestCreateView,
    technicians_list,
    register_technician,
    client_list,
    create_client,
    edit_client,
    delete_client,
    project_list,
    create_project,
    product_list,
    product_detail,
    create_product,
    update_product,
    delete_product,
    price_offer_list,
    price_offer_detail,
    create_price_offer,
    update_price_offer,
    delete_price_offer,
)

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),  # رابط لوحة الإدارة
    path('', home, name='home'),  # رابط الصفحة الرئيسية
    path('register/', register, name='register'),  # رابط التسجيل
    path('maintenance-requests/', maintenance_requests, name='maintenance_requests'),  # رابط طلبات الصيانة
    path('maintenance-requests/add/', MaintenanceRequestCreateView.as_view(), name='create_maintenance_request'),  # رابط إضافة طلب صيانة
    path('technicians/', technicians_list, name='technicians_list'),  # رابط قائمة الفنيين
    path('technicians/register/', register_technician, name='register_technician'),  # رابط تسجيل الفنيين
    path('clients/', client_list, name='client_list'),  # رابط قائمة العملاء
    path('clients/add/', create_client, name='create_client'),  # رابط إضافة عميل
    path('clients/edit/<int:client_id>/', edit_client, name='edit_client'),  # رابط تعديل عميل
    path('clients/delete/<int:client_id>/', delete_client, name='delete_client'),  # رابط حذف عميل
    path('projects/', project_list, name='project_list'),  # رابط قائمة المشاريع
    path('projects/add/', create_project, name='create_project'),  # رابط إضافة مشروع جديد

    # روابط المنتجات
    path('products/', product_list, name='product_list'),  # عرض قائمة المنتجات
    path('products/<int:product_id>/', product_detail, name='product_detail'),  # عرض تفاصيل المنتج
    path('products/add/', create_product, name='create_product'),  # إضافة منتج جديد
    path('products/update/<int:product_id>/', update_product, name='update_product'),  # تعديل منتج
    path('products/delete/<int:product_id>/', delete_product, name='delete_product'),  # حذف منتج

    # روابط عروض الأسعار
    path('price-offers/', price_offer_list, name='price_offer_list'),  # عرض قائمة عروض الأسعار
    path('price-offers/<int:price_offer_id>/', price_offer_detail, name='price_offer_detail'),  # عرض تفاصيل عرض السعر
    path('price-offers/add/', create_price_offer, name='create_price_offer'),  # إضافة عرض سعر جديد
    path('price-offers/update/<int:price_offer_id>/', update_price_offer, name='update_price_offer'),  # تعديل عرض سعر
    path('price-offers/delete/<int:price_offer_id>/', delete_price_offer, name='delete_price_offer'),  # حذف عرض سعر

    # روابط تسجيل الدخول والخروج
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),  # رابط تسجيل دخول
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),  # رابط تسجيل خروج
]
