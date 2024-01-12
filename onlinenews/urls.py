"""
URL configuration for onlinenews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from news import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.dashboard,name='das'),
    path('all/',views.all_news,name='all'),
    path('cate/',views.all_category, name='cate'),
    path('det/<int:id>/',views.detail_news,name='det'),
    path('sig/',views.user_signup,name='sig'),
    path('log/',views.user_login,name='log'),
    path('out/',views.user_logout,name='out'),
    path('add/',views.add_news,name='add'),
    path('up/<int:id>/',views.update,name='up'),
    path('del/<int:id>/',views.delete,name='del'),
    path('pas/',views.change_pass,name='pas')
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
