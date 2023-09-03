from django.contrib import admin
from django.urls import path
from ticket import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.index, name='index'),
    path('index/',views.index, name='index'),
    path('Dashboard/',views.dashboard, name='Dashboard'),
    path('Host/',views.host, name='Host'),
    path('Book/',views.book, name='Book'),
    path('About/',views.about, name='About'),
    path('Booking/',views.booking, name='Booking'),
    path('Host/event_detail.html', views.event_detail,name='Event_detail')
    
]
