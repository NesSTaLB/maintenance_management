from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Client, Technician, AirConditioner, MaintenanceRequest, Project, Product, NewPriceOffer  # تعديل هنا

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('name', 'phone_number')}),  # إضافة الحقول الجديدة هنا
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('name', 'phone_number')}),  # إضافة الحقول عند الإضافة
    )

@admin.register(AirConditioner)
class AirConditionerAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'client', 'installation_date')  # تأكد من وجود هذه الحقول في نموذج AirConditioner
    search_fields = ('brand', 'model')
    list_filter = ('client',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'address')  # تأكد من وجود هذه الحقول في نموذج Client
    search_fields = ('name', 'phone_number')  # إضافة البحث حسب رقم الهاتف
    list_filter = ('address',)

@admin.register(MaintenanceRequest)
class MaintenanceRequestAdmin(admin.ModelAdmin):
    list_display = ('air_conditioner', 'assigned_to', 'request_date', 'status')  # تأكد من وجود هذه الحقول في نموذج MaintenanceRequest
    list_filter = ('status', 'assigned_to')  # إضافة فلتر للحالة والفني المعين
    search_fields = ('air_conditioner__model',)  # البحث حسب نموذج المكيف

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'client', 'start_date', 'end_date')  # تأكد من وجود هذه الحقول في نموذج Project
    search_fields = ('name', 'client__name')  # البحث حسب اسم المشروع واسم العميل
    list_filter = ('start_date', 'end_date')  # إضافة فلتر لتواريخ البدء والانتهاء

# تسجيل نموذج CustomUser مع الإدارة
admin.site.register(CustomUser, CustomUserAdmin)

# تسجيل نموذج Technician
@admin.register(Technician)
class TechnicianAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'phone_number')  # تأكد من وجود هذه الحقول في نموذج Technician
    search_fields = ('name', 'phone_number', 'user__username')  # البحث حسب الاسم ورقم الهاتف

# تسجيل نموذج Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')  # عرض الحقول المطلوبة في قائمة المنتجات
    search_fields = ('name',)  # ميزة البحث عن المنتجات

# تسجيل نموذج NewPriceOffer
@admin.register(NewPriceOffer)  # تعديل هنا
class NewPriceOfferAdmin(admin.ModelAdmin):
    list_display = ('product', 'client', 'discount', 'final_price')  # عرض الحقول المطلوبة في قائمة عروض الأسعار
    search_fields = ('product__name', 'client__name')  # ميزة البحث عن عروض الأسعار
