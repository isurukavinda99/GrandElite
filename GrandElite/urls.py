
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path , include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),


    #login

    path('',include('CAS.urls')),



    #shalitha
    path('emp/', include('employee.urls')),

    #kavinda
    #himasha
    #mihara

    path('demo' , include('demo.urls')),

]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)




if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

