from django.shortcuts import render, get_object_or_404, redirect
from .models import Property, Appointment
from django.db.models import Q
from django.contrib import messages
from .forms import AppointmentForm

def home(request):
    properties = Property.objects.all()

    # Filters
    city = request.GET.get('city')
    state = request.GET.get('state')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if city:
        properties = properties.filter(city__iexact=city)
    if state:
        properties = properties.filter(state__iexact=state)
    if min_price:
        properties = properties.filter(price__gte=min_price)
    if max_price:
        properties = properties.filter(price__lte=max_price)

    # Sorting
    sort_by = request.GET.get('sort_by', 'created_at')
    properties = properties.order_by(sort_by)

    return render(request, 'home.html', {'properties': properties})

def search(request):
    query = request.GET.get('q', '')
    if query:
        properties = Property.objects.filter(title__icontains=query)
    else:
        properties = Property.objects.none()

    return render(request, 'search.html', {'properties': properties})

def property_detail(request, id):
    property = get_object_or_404(Property, id=id)
    return render(request, 'property_detail.html', {'property': property})

def add_to_wishlist(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    wishlist = request.session.get('wishlist', [])
    if property_id not in wishlist:
        wishlist.append(property_id)
        request.session['wishlist'] = wishlist
    return redirect('wishlist')

def remove_from_wishlist(request, property_id):
    wishlist = request.session.get('wishlist', [])
    if property_id in wishlist:
        wishlist.remove(property_id)
        request.session['wishlist'] = wishlist
    return redirect('wishlist')

def wishlist(request):
    wishlist = request.session.get('wishlist', [])
    properties = Property.objects.filter(id__in=wishlist)
    return render(request, 'wishlist.html', {'properties': properties})
def compare_properties(request):
    property_ids = request.GET.getlist('properties')
    properties = Property.objects.filter(id__in=property_ids)
    return render(request, 'compare_properties.html', {'properties': properties})
def schedule_appointment(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.property = property
            if request.user.is_authenticated:
                appointment.user = request.user
            appointment.save()
            messages.success(request, "Your appointment has been scheduled.")
            return redirect('property_detail', property_id=property.id)
    else:
        form = AppointmentForm()

    return render(request, 'schedule_appointment.html', {'form': form, 'property': property})