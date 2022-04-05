# from django.contrib import admin
from django.urls import path
from . import views

app_name = 'country_code_api'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/', views.index, name='index'),
]
