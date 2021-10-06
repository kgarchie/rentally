from django import forms
from .models import House, Images


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['title', 'location', 'price', 'rooms', 'parking']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['image', 'house']
