from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
def list_occupations(request):
    occupations = Occupation.objects.all()
    return render(request, 'main/main.html', {'occupations': occupations})

def occupation_detail(request,pk):
    form = OccupationDetailForm(request.POST)
    if request.method == "POST":
        occupation = form.save(commit=False)
        occupation.save()
        redirect('occupation_page', pk=pk)
    else:
        form = OccupationDetailForm()
        return render(request, 'main/occupation_detail.html', {'form': form})

def occupation_page(request, pk):
    form = OccupationDetailForm(request.POST)
    occupation = get_object_or_404(Occupation, pk=pk)
    if form.is_valid():
        return render(request, 'main/occupation_page.html', {'occupation':occupation})
    else:
        form = OccupationDetailForm()
        return render(request, 'main/occupation_detail.html', {'form': form})