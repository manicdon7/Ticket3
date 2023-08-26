from django.shortcuts import render
from .forms import EventForm

# Create your views here.
def index(request):
    return render(request,"index.html")
def dashboard(request):
    return render(request,"dashboard.html")
def host(request):
    return render(request,"host.html")
def book(request):
    return render(request,"book.html")
def about(request):
    return render(request,"about.html")
def booking(request):
    return render(request,"booking.html")



def index(request):
    events = []
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.cleaned_data
            events.append(event)
    else:
        form = EventForm()
    
    return render(request, 'index.html', {'form': form, 'events': events})
