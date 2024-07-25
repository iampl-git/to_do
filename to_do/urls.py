
from django.contrib import admin
from django.urls import path
from base.views import home, create, edit  # Import views correctly

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('edit/', edit, name='edit'),
]
