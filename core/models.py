from django.contrib.auth.models import AbstractUser
from django.db import models

# نموذج المستخدم المخصص
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, verbose_name='رقم الهاتف')
    name = models.CharField(max_length=100, blank=True, verbose_name='اسم المستخدم')

    def __str__(self):
        return f"{self.name} ({self.username})"

# نموذج العميل
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='اسم العميل')
    phone_number = models.CharField(max_length=15, verbose_name='رقم الهاتف')
    address = models.TextField(verbose_name='العنوان')

    def __str__(self):
        return self.name

# نموذج الفني
class Technician(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name='المستخدم')
    specialization = models.CharField(max_length=100, verbose_name='التخصص')
    phone_number = models.CharField(max_length=15, blank=True, verbose_name='رقم الهاتف')
    name = models.CharField(max_length=100, blank=True, verbose_name='اسم الفني')

    def __str__(self):
        return f"{self.name} - {self.user.username}"

# نموذج جهاز التكييف
class AirConditioner(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='العميل')
    brand = models.CharField(max_length=100, verbose_name='العلامة التجارية')
    model = models.CharField(max_length=100, verbose_name='طراز الجهاز')
    installation_date = models.DateField(verbose_name='تاريخ التركيب')

    def __str__(self):
        return f"{self.brand} {self.model} ({self.client.name})"

# نموذج المشروع
class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name='اسم المشروع')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='العميل')
    start_date = models.DateField(verbose_name='تاريخ البدء')
    end_date = models.DateField(verbose_name='تاريخ الانتهاء')
    description = models.TextField(verbose_name='الوصف')

    def __str__(self):
        return self.name

# نموذج طلب الصيانة
class MaintenanceRequest(models.Model):
    air_conditioner = models.ForeignKey(AirConditioner, on_delete=models.CASCADE, verbose_name='جهاز التكييف')
    assigned_to = models.ForeignKey(Technician, on_delete=models.CASCADE, verbose_name='الفني المعين')
    request_date = models.DateField(auto_now_add=True, verbose_name='تاريخ الطلب')
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'قيد الانتظار'),
        ('In Progress', 'قيد التنفيذ'),
        ('Completed', 'مكتمل')
    ], verbose_name='الحالة')
    description = models.TextField(blank=True, verbose_name='وصف الطلب')

    def __str__(self):
        return f"طلب لصيانة {self.air_conditioner} - الحالة: {self.status}"

# نموذج المنتج
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='اسم المنتج')
    description = models.TextField(verbose_name='وصف المنتج')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='سعر المنتج')
    stock_quantity = models.PositiveIntegerField(verbose_name='الكمية المتوفرة', default=0)
    unit = models.CharField(max_length=50, verbose_name='الوحدة', default='قطعة')
    category = models.CharField(max_length=100, blank=True, null=True, verbose_name='التصنيف')

    def __str__(self):
        return self.name

# نموذج عرض السعر المحدث
class NewPriceOffer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='المنتج')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='العميل')
    offer_date = models.DateField(auto_now_add=True, verbose_name='تاريخ العرض')
    expiration_date = models.DateField(verbose_name='تاريخ انتهاء العرض', null=True, blank=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='الخصم (%)')
    final_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='السعر النهائي', editable=False)
    status = models.CharField(max_length=20, choices=[
        ('Active', 'نشط'),
        ('Expired', 'منتهي الصلاحية'),
        ('Used', 'مستخدم')
    ], verbose_name='حالة العرض', default='Active')

    def save(self, *args, **kwargs):
        # حساب السعر النهائي عند حفظ عرض السعر
        self.final_price = self.product.price * (1 - (self.discount / 100))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"عرض سعر لـ {self.product.name} ({self.client.name})"
