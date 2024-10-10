"""
URL configuration for stemquest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from learning  import views
from django.contrib.auth import views as auth_views
from learning.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index,name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='learning/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('complete/<int:experiment_id>/<int:challenge_id>/', views.complete_progress, name='complete_progress'),
    path('accounts/profile/', views.profile, name='profile'),
    path('experiments/', views.experiments_view, name='experiments'),
    path('codingchallenges/', views.coding_challenges_view, name='coding_challenges'),
]
