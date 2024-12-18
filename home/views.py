from django.shortcuts import render

import geocoder

from user.models import Map_Details
# Create your views here.

# index
def index(request):
    latlng = geocoder.ip('me')
    # if request.user.is_authenticated: 
    #     print(request.user,'User already logged in')
    #     return render(request,'admin/dashboard.html')
    # else:
    print(latlng)
    print(latlng.ip)
    print(latlng.lat)
    print(latlng.lng)

    map_db = Map_Details.objects.all()
    return render(request,'home/home.html',{'lat':latlng.lat, 'lng':latlng.lng, 'map_db': map_db})

from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home.index')  # Success redirect
    else:
        form = ContactForm()

    return render(request, 'home/contact_us.html', {'form': form})


from django.shortcuts import render, get_object_or_404
from .models import Pet

def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    context = {
        'pet': pet
    }
    return render(request, 'user/pet_detail.html', context)





# map for listing all dog spots
def map(request):
    latlng = geocoder.ip('me')

    map_db = Map_Details.objects.all()
    context = {'map_db': map_db, 'lat':latlng.lat, 'lng':latlng.lng}
    return render(request, 'home/map.html', context)


def donation(request):
    context = {}
    return render(request, 'home/donation.html', context)



from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Pet, Adoption
from django.db.models import Q


from django.db.models import Q
from django.core.paginator import Paginator
from .models import Pet, Adoption
from django.shortcuts import render
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Pet, Adoption

from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Pet

def pet_listing(request):
    # Get the search query from the GET parameters (search_based features)
    query = request.GET.get('q', '').strip()  # Default to an empty string if no query is provided
    
    # Fetch all pets by default
    pets = Pet.objects.all()

    # If a search query is provided, filter pets based on the query
    if query:
        pets = pets.filter(
            Q(pet_name__icontains=query) |
            Q(pet_breed__icontains=query) |
            Q(pet_type__icontains=query)
        )

    # Pagination: 10 pets per page
    paginator = Paginator(pets, 10)
    page_number = request.GET.get('page', 1)  # Get the current page number
    pets_page = paginator.get_page(page_number) 

    context = {
        'pets': pets_page,  # Paginated pets
        'query': query,     # The search query to populate the search bar
    }

    return render(request, 'user/dashboard.html', context)





# Adopt Pet View
@login_required
def adopt_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id, pet_status='Available')

    if request.method == 'POST':
        # Mark the pet as adopted
        pet.pet_status = 'Adopted'
        pet.date_adopted = timezone.now()
        pet.save()

        # Create an adoption record
        Adoption.objects.create(user=request.user, pet=pet, adoption_confirmed=True)

        return redirect('home.pet_listing')

    context = {
        'pet': pet
    }

    return render(request, 'user/adopt_pet.html', context)


# View to show the user's adoptions
@login_required
def my_adoptions(request):
    # Fetch the pets adopted by the current logged-in user
    adoptions = Adoption.objects.filter(user=request.user)

    context = {
        'adoptions': adoptions
    }

    return render(request, 'user/adopt_list.html', context)


from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Pet, Adoption
from django.db.models import Q

from django.db.models import Q
from django.db.models.functions import Replace
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from django.db.models.functions import Replace
from .models import Pet
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Pet


