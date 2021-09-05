
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),

    #shalitha
    path('emp/', include('employee.urls')),

    #kavinda
    path('isms/' , include('ISMS.urls')),
    #himasha
    #mihara
    path('rae/', include('RAE.urls')),


    path('demo' , include('demo.urls')),

]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

