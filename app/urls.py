from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import login_view, logout_view, register_view
from cars.views import (
    CarDeleteView,
    CarDetailView,
    CarsListView,
    CarUpdateView,
    NewCarCreateView,
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('cars/', CarsListView.as_view(), name='cars_list'),
    path('cars/new/', NewCarCreateView.as_view(), name='new_car'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('cars/<int:pk>/update', CarUpdateView.as_view(), name='car_update'),
    path('cars/<int:pk>/delete', CarDeleteView.as_view(), name='car_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
