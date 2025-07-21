from django import forms
from .models import Venue
from .models import BookingEnquiry


class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'code', 'capacity', 'image']


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingEnquiry
        fields = ['title', 'venue', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

