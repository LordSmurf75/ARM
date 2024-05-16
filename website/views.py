from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import KoncertForm
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout
from .models import Bestyrelse, Koncert, Frivillig, Spillested
from .forms import KoncertForm, SpillestedForm
from django.contrib.auth.models import User


def bestyrelse(request,pk):
	bestyrelse = Bestyrelse.objects.get(id=pk)
	return render(request, 'bestyrelse.html', {'bestyrelse':bestyrelse})


def home(request):
	current_date = timezone.now()
	concerts = Koncert.objects.filter(dato__gte=current_date).order_by('dato')
	return render(request, 'home.html', {'concerts':concerts})


def spillede_koncerter(request):
    spillede_koncerter = Koncert.objects.filter(dato__lt=timezone.now()).order_by('-dato')
    return render(request, 'spillede_koncerter.html', {'spillede_koncerter': spillede_koncerter})


def about(request):
	members = Bestyrelse.objects.all().order_by('id')
	return render(request, 'about.html', {'members':members})


def frivillig(request):
	frivillige = Frivillig.objects.all()
	return render(request, 'frivillig.html', {'frivillige':frivillige})


def vagter(request,pk):
	vagter = Frivillig.objects.get(id=pk)
	return render(request, 'vagter.html', {'vagter':vagter})


def spillested(request):
	spillesteder = Spillested.objects.all()
	return render(request, 'spillesteder.html', {'spillesteder':spillesteder})


def opret_koncert(request):
    if request.method == 'POST':
        form = KoncertForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect hvor som helst du ønsker efter oprettelsen
    else:
        form = KoncertForm()
    return render(request, 'opret_koncert.html', {'form': form})


def opret_spillested(request):
	if request.method == "POST":
		form = SpillestedForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = SpillestedForm()
	return render(request, 'opret_spillested.html', {'form': form})


def rediger_koncert(request, pk):
    # Hent den specifikke koncert fra databasen
    koncert = get_object_or_404(Koncert, pk=pk)
    # Hvis der er indsendt en formular
    if request.method == 'POST':
        # Instantier formen med de indsendte data og den eksisterende instans af Koncert
        form = KoncertForm(request.POST, instance=koncert)
        # Hvis formen er gyldig
        if form.is_valid():
            # Gem ændringerne i databasen
            form.save()
            # Redirect til en bekræftelsesside eller en liste over koncerter
            return redirect('home')
    else:
        # Hvis det er en GET-anmodning, instantier formen med den eksisterende instans af Koncert
        form = KoncertForm(instance=koncert)
    
    # Send formen til skabelonen sammen med den specifikke koncert
    return render(request, 'edit.html', {'form': form, 'koncert': koncert})


# Dekorer funktionen med require_POST for kun at tillade POST-anmodninger
@require_POST
def slet_koncert(request, koncert_id):
    # Hent koncertobjektet fra databasen eller returner en 404-fejl, hvis det ikke findes
    koncert = get_object_or_404(Koncert, id=koncert_id)
    
    # Slet koncerten fra databasen
    koncert.delete()
    
    # Omdiriger brugeren til en passende side efter sletning, f.eks. koncertlisten
    return redirect('home')  # 'koncert_liste' er URL-navnet til listen over koncerter


def band_list(request):
    bands = set()
    koncerter = Koncert.objects.all()
    
    for koncert in koncerter:
        if koncert.band1:
            bands.add(koncert.band1)
        if koncert.band2:
            bands.add(koncert.band2)
        if koncert.band3:
            bands.add(koncert.band3)
        if koncert.band4:
            bands.add(koncert.band4)
        if koncert.band5:
            bands.add(koncert.band5)
        if koncert.band6:
            bands.add(koncert.band6)
        if koncert.band7:
            bands.add(koncert.band7)
        if koncert.band8:
            bands.add(koncert.band8)
    
    bands_list = sorted(bands)
    bands_count = len(bands_list)
    
    return render(request, 'band_list.html', {'bands': bands_list, 'bands_count': bands_count})
    

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Du er nu logget ind"))
            return redirect('home')
        else:
            messages.success(request, ("Der var et problem med at logge dig ind... Prøv igen..."))
            return redirect('login')
    else:   
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("Du er blevet logget ud"))
    return redirect('home')