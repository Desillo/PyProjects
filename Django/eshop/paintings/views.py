from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Painting
from django.http import Http404
from django.views import generic
# Create your views here.


class PaintingListView(generic.ListView):
    model = Painting
    
    def get_queryset(self) -> QuerySet[Any]:
        return Painting.objects.order_by("-pub_date")[:5]
    
class PaintingDetailView(generic.DetailView):
    model = Painting

    

def index(request):
    latest_paint_list = Painting.objects.order_by("-pub_date")[:5]
    context = {"latest_paint_list" : latest_paint_list }
    return render(request, "paintings/index.html", context)

def detail(request, paint_id):
    try:
        paint = Painting.objects.get(pk=paint_id)
    except Painting.DoesNotExist:
        raise Http404("Painting does not exist")
    return render(request, "paintings/painting_detail.html", {"painting" : paint})
