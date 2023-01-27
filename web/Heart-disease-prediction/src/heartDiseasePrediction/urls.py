"""heartDiseasePrediction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from os import name, pathsep
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import pages



#custom pages
from pages.views import home_view, result_view, user_heart_info_view, footer_view, prediction_page_view, header_view, user_heart_info_save_display_view

urlpatterns = [
    #create diff pages and route that here like contact etc
    path('',home_view,name='home'),
    path('home/', home_view, name='home'),
    path('result/', result_view, name='result'),
    path('userInfo/', user_heart_info_view, name='userInfo'),
    path('footer/', footer_view, name='footer'),
    path('prediction/', prediction_page_view, name='prediction'),
    path('header/', header_view, name='header'),
    path('userHeartInfoSaveDisplay/', user_heart_info_save_display_view, name='userHeartInfoSaveDisplay'),
    path('admin/', admin.site.urls),
]



