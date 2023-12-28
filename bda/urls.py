"""
URL configuration for bda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView

from clonus import views
from clonus.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("compare/", views.compare, name="compare"),
    path("compare_many/", views.compare_many, name="compare_many"),
    path("summary/<str:h>", views.summary, name="summary"),
    path("summary_many/<str:h>", views.summary_many, name="summary_many"),
    path("list/", views.list, name="list"),
    path("login/", ClonusLoginView.as_view(), name='login'),
    path('register/', ClonusRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
