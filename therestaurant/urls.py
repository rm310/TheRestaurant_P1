from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

def index(request):
    return render(request, 'restaurantsystem/index.html')

# URL tilni o‘zgartirish uchun
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # <-- til almashtirish uchun kerak
]

# I18N URL lar (tilni URL orqali boshqarish)
urlpatterns += i18n_patterns(
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('', include('restaurantsystem.urls')),
    path('accounts/', include('accounts.urls')),
)

# Static va Media fayllar
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
