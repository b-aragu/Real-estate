from django.contrib import admin
from .models import Property, PropertyMedia

class PropertyMediaInline(admin.TabularInline):
    model = PropertyMedia
    extra = 1  # Number of empty forms to display by default

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'address', 'city', 'state', 'zip_code')
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zip_code')
    inlines = [PropertyMediaInline] 

@admin.register(PropertyMedia)
class PropertyMediaAdmin(admin.ModelAdmin):
    list_display = ('property', 'media_type', 'file')
    search_fields = ('property__title', 'media_type')
    fields = ('property', 'media_type', 'file') 
