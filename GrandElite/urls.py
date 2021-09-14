from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # shalitha
    # kavinda
    # himasha
    path('pms/', include('employeePayments.urls')),

    path('allowances/', include('allowances.urls')),
    path('deductions', include('deductions.urls')),
    path('sp', include('supplierPayments.urls')),
    # path('employeePayments', include('employeePayments.urls')),

    # mihara

    path('demo', include('demo.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
