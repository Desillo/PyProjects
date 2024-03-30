from django.urls import path
from . import views

urlpatterns = [
    #path("", views.index, name="index"), 
    path("", views.PaintingListView.as_view(), name="paintings"), 
    path("<int:pk>/", views.PaintingDetailView.as_view(), name="painting-detail"),   
]