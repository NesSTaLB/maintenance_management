from pathlib import Path
import os

# بناء المسارات داخل المشروع.
BASE_DIR = Path(__file__).resolve().parent.parent

# إعدادات سريعة للتطوير.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-default-secret-key')  # استخدم بيئة التشغيل للإعدادات الحساسة

DEBUG = False  # يجب تغييره إلى False في بيئة الإنتاج!
ALLOWED_HOSTS = ['127.0.0.1', '', '', '']  # استبدل بنطاقك الفعلي

# تعريف التطبيقات
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # إضافة التطبيق الجديد
    'admin_interface',  # إضافة مكتبة admin-interface
    'colorfield',  # إضافة colorfield هنا
]

AUTH_USER_MODEL = 'core.CustomUser'  # تعيين نموذج المستخدم المخصص

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # تأكد من إضافة هذا السطر
]

ROOT_URLCONF = 'maintenance_management.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # إضافة مسار القوالب المخصصة
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'maintenance_management.wsgi.application'

# إعدادات قاعدة البيانات
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # استخدام MySQL
        'NAME': 'u563499713_houssam',          # اسم قاعدة البيانات
        'USER': 'u563499713_hd',               # اسم المستخدم
        'PASSWORD': os.environ.get('DB_PASSWORD', '03420368Hh@@'),  # استخدم البيئة للإعدادات الحساسة
        'HOST': 'srv1294.hstgr.io',              # مضيف خادم MySQL
        'PORT': '3306',                         # المنفذ الافتراضي لـ MySQL
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",  # تفعيل وضع القواعد الصارمة
        },
    }
}

# إعدادات البريد الإلكتروني
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'  # استبدلها بمزود البريد الإلكتروني الخاص بك
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_password'
DEFAULT_FROM_EMAIL = 'your_email@example.com'

# التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# الدولية (Internationalization)
LANGUAGE_CODE = 'ar'  # تعيين اللغة إلى العربية
TIME_ZONE = 'Asia/Riyadh'  # تعيين المنطقة الزمنية إلى الرياض
USE_I18N = True
USE_TZ = True

# إعدادات تسجيل الدخول
LOGIN_REDIRECT_URL = 'maintenance_requests'  # إعادة التوجيه إلى صفحة طلبات الصيانة
LOGOUT_REDIRECT_URL = 'home'  # إعادة التوجيه بعد تسجيل الخروج

# إعدادات الملفات الثابتة
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
    BASE_DIR / 'core/static',
]  

# إعدادات الوسائط (Media)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # مسار حفظ الملفات المرفوعة

# نوع حقل المفتاح الأساسي الافتراضي
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
