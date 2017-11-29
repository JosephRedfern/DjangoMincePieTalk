from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Pie
from .forms import RateForm

def details(request, pie_id):
    pie = Pie.objects.filter(id=pie_id).first()
    return render(request, 'details.html', {'pie': pie})
    
def list_all(request):
    pies = Pie.objects.all()
    return render(request, 'list_all.html', {'pies': pies})
    
def rate(request):
    print(request.user)
    if request.method == 'POST':
        form = RateForm(request.POST)
        
        if form.is_valid():
            rating = form.save(commit=False)
            rating.creator = request.user
            rating.save()
            return HttpResponseRedirect('/p/{}'.format(rating.pie.id))
    else:
        form = RateForm()
        return render(request, 'rate.html', {'form': form})
