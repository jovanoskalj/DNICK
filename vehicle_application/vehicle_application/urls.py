from django.contrib import admin
from django.urls import path
from vehicle import views as views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name="index"),
    path('product/<int:car_id>/', views.car_details, name='details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
