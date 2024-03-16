from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserProfileForm


# Create your views here.
def home_page_view(request):
    return render(request, 'homepage.html')

def landing_page_view(request):
    return render(request, 'landingpage.html')

def self_employment_page_view(request):
    return render(request, 'self_employment.html')

def courses_page_view(request):
    return render(request, 'courses.html')

def employers_page_view(request):
    return render(request, 'employers.html')

def profile_page_view(request):
    form = UserProfileForm() 
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('update_profile') 
    else:
        form = UserProfileForm()
    return render(request, 'profile.html', {'form': form})

def update_profile_page_view(request):
    return render(request, 'update_profile.html')