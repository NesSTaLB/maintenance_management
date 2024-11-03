from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, verbose_name='رقم الهاتف')  # حقل إضافي لرقم الهاتف
    name = models.CharField(max_length=100, blank=True, verbose_name='اسم المستخدم')  # حقل لاسم المستخدم

    def __str__(self):
        return f"{self.name} ({self.username})"  # تمثيل نصي للمستخدم

class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='اسم العميل')  # اسم العميل
    phone_number = models.CharField(max_length=15, verbose_name='رقم الهاتف')  # رقم هاتف العميل
    address = models.TextField(verbose_name='العنوان')  # عنوان العميل

    def __str__(self):
        return self.name  # تمثيل نصي للعميل

class Technician(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name='المستخدم')  # ربط الفني بالمستخدم المخصص
    specialization = models.CharField(max_length=100, verbose_name='التخصص')  # تخصص الفني
    phone_number = models.CharField(max_length=15, blank=True, verbose_name='رقم الهاتف')  # رقم هاتف الفني
    name = models.CharField(max_length=100, blank=True, verbose_name='اسم الفني')  # اسم الفني

    def __str__(self):
        return f"{self.name} - {self.user.username}"  # تمثيل نصي للفني

class AirConditioner(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='العميل')  # ربط جهاز التكييف بالعميل
    brand = models.CharField(max_length=100, verbose_name='العلامة التجارية')  # العلامة التجارية لجهاز التكييف
    model = models.CharField(max_length=100, verbose_name='طراز الجهاز')  # طراز جهاز التكييف
    installation_date = models.DateField(verbose_name='تاريخ التركيب')  # تاريخ تركيب الجهاز

    def __str__(self):
        return f"{self.brand} {self.model} ({self.client.name})"  # تمثيل نصي لجهاز التكييف

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='اسم المنتج')  # اسم المنتج
    description = models.TextField(blank=True, verbose_name='وصف المنتج')  # وصف المنتج
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='السعر')  # سعر المنتج

    def __str__(self):
        return self.name  # تمثيل نصي للمنتج

class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name='اسم المشروع')  # اسم المشروع
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='العميل')  # ربط المشروع بالعميل
    start_date = models.DateField(verbose_name='تاريخ البدء')  # تاريخ بدء المشروع
    end_date = models.DateField(verbose_name='تاريخ الانتهاء')  # تاريخ انتهاء المشروع
    description = models.TextField(verbose_name='الوصف')  # وصف المشروع

    def __str__(self):
        return self.name  # تمثيل نصي للمشروع

class MaintenanceRequest(models.Model):
    air_conditioner = models.ForeignKey(AirConditioner, on_delete=models.CASCADE, verbose_name='جهاز التكييف')  # ربط طلب الصيانة بجهاز التكييف
    assigned_to = models.ForeignKey(Technician, on_delete=models.CASCADE, verbose_name='الفني المعين')  # ربط الطلب بالفني
    request_date = models.DateField(auto_now_add=True, verbose_name='تاريخ الطلب')  # تاريخ تقديم الطلب
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'قيد الانتظار'),
        ('In Progress', 'قيد التنفيذ'),
        ('Completed', 'مكتمل')
    ], verbose_name='الحالة')  # حالة الطلب
    description = models.TextField(blank=True, verbose_name='وصف الطلب')  # وصف الطلب

    def __str__(self):
        return f"طلب لصيانة {self.air_conditioner} - الحالة: {self.status}"  # تمثيل نصي لطلب الصيانة
