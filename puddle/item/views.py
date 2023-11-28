from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Item

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=item.pk)[0:3]
    context = {
        'item': item,
        'related_items': related_items,
    }
    return render(request, 'item/detail.html', context)