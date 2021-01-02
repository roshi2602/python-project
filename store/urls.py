"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.conf.urls import include,url
from django.conf import settings

from productapp import views
from coupon import views
from employee import views
from attendence import views
from payroll import views
from partner import views
from promotions import views
from customer import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('employee.urls')),
    path('product/', include('productapp.urls')),
    path('coupon/',include('coupon.urls')),
    path('user/', include('userapp.urls')),
    path('attendence/',include('attendence.urls')),
    path('', include('payroll.urls')),
    path('partner/', include('partner.urls')),
    path('promotions/', include('promotions.urls')),
    path('customer/', include('customer.urls')),
   
   

 ]
   