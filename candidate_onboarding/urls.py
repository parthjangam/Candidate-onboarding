"""
URL configuration for candidate_onboarding project.

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
from onboarding_app import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('', views.upload_form, name='upload_form'),  # Upload form page
    path('candidates/', views.candidate_list, name='candidate_list'),  # New view to list candidates
    path('delete/<int:candidate_id>/', views.delete_candidate, name='delete_candidate'),
    path('delete_all/', views.delete_all_candidates, name='delete_all_candidates'),

]
