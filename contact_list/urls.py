from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/<int:contact_id>', views.SingleContactView.as_view(), name='contact'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
