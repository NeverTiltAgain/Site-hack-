"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import django_project
from . import views
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView # new


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("", TemplateView.as_view(template_name="Профиль.html"), name="home"),
    path('База-знаний.html', views.bz),
    path('Достижения.html', views.achievements),
    path('Карта-прогресса.html', views.progress_map),
    path('Карточка-ячейки-прогресса.html', views.progress_cell_card),
    path('Карточка-второй-ячейки.html', views.Second_cell_card),
    path('Карточка-третьей-ячейки.html', views.third_cell_card),
    path('Контакты.html', views.contacts),
    path('Мероприятия.html', views.events),
    path('Профиль.html', views.profile),

]
