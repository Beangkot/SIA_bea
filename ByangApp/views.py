from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import LostFoundItemForm
from .models import LostFoundItem


def dashboard(request):
    try:
        total_items = LostFoundItem.objects.count()
        lost_items = LostFoundItem.objects.filter(status='Lost').count()
        found_items = LostFoundItem.objects.filter(status='Found').count()
        claimed_items = LostFoundItem.objects.filter(status='Claimed').count()

        recent_items = LostFoundItem.objects.all().order_by('-id')[:5]

        dashboard_items = [
            {
                'id': f"LF-{item.item_id}",
                'name': item.item_name,
                'category': item.category,
                'status': item.status,
                'location': item.location,
                'description': item.description,
                'dateReported': (
                    item.date_reported.isoformat()
                    if item.date_reported else ''
                ),
                'contactName': item.contact_name,
                'contactInfo': item.contact_information,
                'image': item.item_image.url if item.item_image else '',
            }
            for item in LostFoundItem.objects.all().order_by(
                '-date_reported', '-item_id'
            )
        ]

    except Exception:
        total_items = 0
        lost_items = 0
        found_items = 0
        claimed_items = 0
        recent_items = []
        dashboard_items = []

    context = {
        'total_items': total_items,
        'lost_items': lost_items,
        'found_items': found_items,
        'claimed_items': claimed_items,
        'recent_items': recent_items,
        'dashboard_items': dashboard_items,
    }

    return render(
        request,
        'Inv_Items/dashboard.html',
        context
    )


def item_list(request):
    search = request.GET.get('search', '').strip()
    selected_status = request.GET.get('status', '')
    selected_category = request.GET.get('category', '')

    items = LostFoundItem.objects.all().order_by('-date_reported')

    if search:
        items = items.filter(
            Q(item_name__icontains=search)
            | Q(description__icontains=search)
            | Q(location__icontains=search)
        )

    if selected_status:
        items = items.filter(status=selected_status)

    if selected_category:
        items = items.filter(category=selected_category)

    context = {
        'items': items,
        'search': search,
        'selected_status': selected_status,
        'selected_category': selected_category,
    }

    return render(
        request,
        'Inv_Items/item_list.html',
        context
    )


def item_detail(request, pk):
    item = get_object_or_404(LostFoundItem, pk=pk)

    return render(
        request,
        'Inv_Items/item_detail.html',
        {'item': item}
    )


def item_create(request):
    if request.method == 'POST':
        form = LostFoundItemForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            item = form.save()
            return redirect('item_detail', pk=item.pk)

    else:
        form = LostFoundItemForm()

    return render(
        request,
        'item_form.html',
        {
            'form': form,
            'page_title': 'Report a Lost or Found Item'
        }
    )


def item_update(request, pk):
    item = get_object_or_404(LostFoundItem, pk=pk)

    if request.method == 'POST':
        form = LostFoundItemForm(
            request.POST,
            request.FILES,
            instance=item
        )

        if form.is_valid():
            form.save()
            return redirect('item_detail', pk=item.pk)

    else:
        form = LostFoundItemForm(instance=item)

    return render(
        request,
        'item_form.html',
        {
            'form': form,
            'page_title': 'Update Item'
        }
    )


def item_delete(request, pk):
    item = get_object_or_404(LostFoundItem, pk=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('item_list')

    return render(
        request,
        'item_confirm_delete.html',
        {'item': item}
    )