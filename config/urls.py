"""
URL configuration for blockchain_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from main_app.views import mainpage_view, lessons_list_view, step_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainpage_view, name='main_page'),
    path('lessons/', lessons_list_view, name='lessons_list'),
    path('lessons/<str:lesson_slug>/<str:step_slug>/', step_detail_view, name='step_detail')
]
