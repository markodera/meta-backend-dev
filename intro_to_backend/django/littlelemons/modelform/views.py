from django.shortcuts import render
from .forms import TestForm

def index(request):
    form = TestForm()
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            form = TestForm()
            return render(request, 'modelform/index.html', {'form': form})
        return render(request, 'modelform/index.html', {'form': form})
    
    return render(request, 'modelform/index.html', {'form': form})