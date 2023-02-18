from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

# Create your views here.
from item.models import Item


@login_required
def index(request):
    items = Item.objects.filter(create_by=request.user)
    print(items)

    return render(request, 'dashboard/index.html', {
        'items': items
    })
