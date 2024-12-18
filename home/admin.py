from django.contrib import admin
from .models import Pet, Adoption, Contact

# Admin view for the Pet model
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('pet_name', 'pet_breed', 'pet_age', 'pet_status', 'pet_gender', 'pet_type', 'date_added', 'date_adopted')
    list_filter = ('pet_status', 'pet_breed', 'pet_gender', 'pet_size', 'health_status', 'pet_type')
    search_fields = ('pet_name', 'pet_breed', 'pet_status', 'location_city', 'pet_type')
    readonly_fields = ('date_added', 'date_adopted')
    fieldsets = (
        ('Basic Information', {
            'fields': ('pet_name', 'pet_breed', 'pet_age', 'pet_status', 'pet_gender', 'pet_type', 'pet_size', 'pet_color', 'image')
        }),
        ('Health & Vaccination', {
            'fields': ('health_status', 'vaccinated', 'spayed_neutered', 'special_needs')
        }),
        ('Location', {
            'fields': ('location_city', 'location_latitude', 'location_longitude')
        }),
        ('Timestamps', {
            'fields': ('date_added', 'date_adopted')
        }),
    )

# Admin view for the Adoption model
@admin.register(Adoption)
class AdoptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'pet', 'adoption_date', 'adoption_confirmed')
    list_filter = ('adoption_confirmed',)
    search_fields = ('user__username', 'pet__pet_name')
    readonly_fields = ('adoption_date',)

# Admin view for the Contact model
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at', 'message')
    search_fields = ('name', 'email', 'subject', 'message')
