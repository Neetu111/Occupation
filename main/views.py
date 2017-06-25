from django.shortcuts import render,get_object_or_404
from .models import Occupation

def list_occupations(request):
    occupations = Occupation.objects.all()
    return render(request, 'main/main.html', {'occupations': occupations})

def occupation_detail(request, pk):
    occupation = get_object_or_404(Occupation, pk=pk)
    return render(request, 'main/occupation_detail.html',{'occupation': occupation})