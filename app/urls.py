from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import login_view, logout_view, register_view
from cars import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('cars/', views.cars_view, name='cars_list'),
    path('cars/new/', views.new_car_view, name='new_car'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
