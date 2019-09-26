"""movie_review URL Configuration

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
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^registration/', views.registration, name='registration'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^edit_profile/', views.edit_profile, name='edit_profile'),
    url(r'^change_password/', views.change_password, name='change_password'),
    url(r'^search/', views.search, name='search'),
    url(r'^movie_list/', views.movie_list, name='movie_list'),
    url(r'^movie_detail/(?P<id>\d+)/(?P<movie_name>[\w -:.%]+)/$', views.movie_detail, name='movie_detail'),
    url(r'^about/', views.about_us, name='about')
]
