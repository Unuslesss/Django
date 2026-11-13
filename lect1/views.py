from django.shortcuts import render

def home_view(request):
    return render(request, 'lect1/home.html')

def contacts_view(request):
    return render(request, 'lect1/contacts.html')

def location_view(request):
    return render(request, 'lect1/location.html')

def programs_view(request):
    return render(request, 'lect1/programs.html')

def timetable_view(request):
    return render(request, 'lect1/timetable.html')
