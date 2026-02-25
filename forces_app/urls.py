"""
URL configuration for forces_app project.

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
from wh_40k import views as wh40k_views
from wh_old_world import views as old_world_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wh40k/<int:faction_id>/', wh40k_views.ForceOrgView.as_view(), name='wh40k'),
    path('wh40k-factions/', wh40k_views.FactionsView.as_view(), name='wh40k-factions'),
    path('wh-old-world/', old_world_views.OldWorldView.as_view(), name='wh-old-world'),
    path('owfactions/', old_world_views.OldWorldFactionsView.as_view(), name='owfactions'),
]
