from django.forms import ModelForm
from .models import Pie, Rating

class RateForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['pie', 'pastry', 'filling', 'comments']
