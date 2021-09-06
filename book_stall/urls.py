"""book_stall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from book.views import *
from subscribe.views import subscribe_email
from book import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.homepage, name="home"),
    path('show-books/', views.show_book, name="stock"),
    path('hard-delete-book/<int:id>', views.hard_delete_book, name="hard-delete"),
    path('soft-delete-book/<int:id>', views.soft_delete_book, name="soft-delete"),
    path('update-book/<int:id>', views.edit_book, name="edit"),
    path('active-book/', views.active_book, name="active-books"),
    path('inactive-book/', views.inactive_book, name="inactive-books"),
    path('restore-book/<int:id>', views.restore_book, name="restore-books"),
    path('email-home/', subscribe_email, name="subscribe_email"),

]
