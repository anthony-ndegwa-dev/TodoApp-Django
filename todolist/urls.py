"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name="home"),
    path('saved', views.saved_view, name="saved"),
    path('search', views.SearchResultsView.as_view(), name="search_results"),
    path('searched', views.SearchResults.as_view(), name="searched_results"),
    path('searchdate', views.Leo.as_view(), name="searched_date"),
    path('edit/<int:id>', views.edit),
    path('delete/<int:id>', views.destroy),
    path('update/<int:id>', views.update),
]
