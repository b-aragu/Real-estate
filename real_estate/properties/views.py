from django.shortcuts import render
from .models import Property
from django.shortcuts import get_object_or_404, render

def home(request):
    properties = Property.objects.all()
    return render(request, 'home.html', {'properties': properties})
def search(request):
    query = request.GET.get('q', '')  # Default to an empty string if 'q' is None
    if query:
        properties = Property.objects.filter(title__icontains=query)
    else:
        properties = Property.objects.none()  # Return an empty queryset if no query

    return render(request, 'search.html', {'properties': properties})
def property_detail(request, id):
    property = get_object_or_404(Property, id=id)
    return render(request, 'property_detail.html', {'property': property})
