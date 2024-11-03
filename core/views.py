from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views import View
from django.core.mail import send_mail
from django.db.models import Q
from .models import MaintenanceRequest, Technician, Client, Project, Product, NewPriceOffer
from .forms import (
    MaintenanceRequestForm, 
    TechnicianForm, 
    ClientForm, 
    CustomUserCreationForm, 
    ProjectForm, 
    ProductForm, 
    PriceOfferForm
)

# عرض الصفحة الرئيسية
def home(request):
    return render(request, 'core/index.html')

# عرض تسجيل المستخدمين
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('maintenance_requests')
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/register.html', {'form': form})

# عرض طلبات الصيانة
@login_required
def maintenance_requests(request):
    requests = MaintenanceRequest.objects.all()
    return render(request, 'core/maintenance_requests.html', {'requests': requests})

# إنشاء طلب صيانة جديد باستخدام View
class MaintenanceRequestCreateView(View):
    def get(self, request):
        form = MaintenanceRequestForm()
        return render(request, 'core/create_maintenance_request.html', {'form': form})

    def post(self, request):
        form = MaintenanceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maintenance_requests')
        return render(request, 'core/create_maintenance_request.html', {'form': form})

# عرض قائمة الفنيين
@login_required
def technicians_list(request):
    technicians = Technician.objects.all()
    return render(request, 'core/technicians_list.html', {'technicians': technicians})

# عرض تسجيل فني جديد
def register_technician(request):
    if request.method == 'POST':
        user_form = TechnicianForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            specialization = user_form.cleaned_data.get('specialization')
            Technician.objects.create(user=user, specialization=specialization)
            return redirect('technicians_list')
    else:
        user_form = TechnicianForm()
    return render(request, 'core/register_technician.html', {'form': user_form})

# عرض قائمة العملاء مع ميزة البحث
@login_required
def client_list(request):
    query = request.GET.get('search', '')
    clients = Client.objects.filter(Q(name__icontains=query) | Q(phone_number__icontains=query)) if query else Client.objects.all()
    return render(request, 'core/client_list.html', {'clients': clients, 'search': query})

# إنشاء عميل جديد مع إرسال إشعار بريد إلكتروني
def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            send_mail(
                'عميل جديد تم إضافته',
                f'تم إضافة عميل جديد: {client.name}',
                'your_email@example.com',
                ['recipient@example.com'],
                fail_silently=False,
            )
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'core/create_client.html', {'form': form})

# تعديل عميل
def edit_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'core/edit_client.html', {'form': form, 'client': client})

# حذف عميل
def delete_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'core/delete_client.html', {'client': client})

# عرض قائمة المشاريع
@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'core/projects/project_list.html', {'projects': projects})

# إنشاء مشروع جديد
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'projects/create_project.html', {'form': form})

# عرض قائمة المنتجات
@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'core/product_list.html', {'products': products})

# تفاصيل المنتج
@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'core/product_detail.html', {'product': product})

# إضافة منتج جديد
@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'core/create_product.html', {'form': form})

# تعديل منتج
@login_required
def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'core/update_product.html', {'form': form, 'product': product})

# حذف منتج
@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'core/delete_product.html', {'product': product})

# عرض قائمة عروض الأسعار
@login_required
def price_offer_list(request):
    offers = NewPriceOffer.objects.all()
    return render(request, 'core/price_offer_list.html', {'offers': offers})

# تفاصيل عرض السعر
@login_required
def price_offer_detail(request, price_offer_id):
    offer = get_object_or_404(NewPriceOffer, id=price_offer_id)
    return render(request, 'core/price_offer_detail.html', {'offer': offer})

# إضافة عرض سعر جديد
@login_required
def create_price_offer(request):
    if request.method == 'POST':
        form = PriceOfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.final_price = offer.product.price * (1 - offer.discount / 100)
            offer.save()
            return redirect('price_offer_list')
    else:
        form = PriceOfferForm()
    return render(request, 'core/create_price_offer.html', {'form': form})

# تعديل عرض السعر
@login_required
def update_price_offer(request, price_offer_id):
    offer = get_object_or_404(NewPriceOffer, id=price_offer_id)
    if request.method == 'POST':
        form = PriceOfferForm(request.POST, instance=offer)
        if form.is_valid():
            form.save()
            return redirect('price_offer_list')
    else:
        form = PriceOfferForm(instance=offer)
    return render(request, 'core/update_price_offer.html', {'form': form, 'offer': offer})

# حذف عرض السعر
@login_required
def delete_price_offer(request, price_offer_id):
    offer = get_object_or_404(NewPriceOffer, id=price_offer_id)
    if request.method == 'POST':
        offer.delete()
        return redirect('price_offer_list')
    return render(request, 'core/delete_price_offer.html', {'offer': offer})
