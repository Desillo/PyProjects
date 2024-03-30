"""
URL configuration for django1 project.

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
from django.urls import path, include
from django.urls import re_path
from hello import views

prod_patterns = [
    path('new', views.new),
    path('top', views.top),
    path('', views.products),   
]

prod_id_patterns = [
    path('comment', views.comment_id),
    path('question', views.question_id),
    path('', views.product_id),  
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('product/', include(prod_patterns)),
    path('product/<int:id>/', include(prod_id_patterns)),
    path('index2', views.index2),
    path('user/<str:name>/<int:age>', views.user),
    path('user/<str:name>', views.user),
    path('user/<int:age>', views.user),
    path('user/', views.user),
    re_path(r'^about', views.about, kwargs={'name' : 'Tom', 'age' : 38}),
    re_path(r'^contact', views.contact),
    path('index3/<int:id>/', views.index3),
    path('access/<int:age>/', views.access),
    path('details/', views.details),
    path('index4/', views.index4),
    path('get/', views.get),
    path('set/', views.set),
    path('index5/<str:name>/<str:age>', views.index5),
    path('index5/', views.index5),

]
