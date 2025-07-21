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
        fields = ['title', 'start_date', 'end_date', 'venues']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'venues': forms.SelectMultiple(),
        }

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('start_date')
        end = cleaned_data.get('end_date')
        selected_venues = cleaned_data.get('venues')

        if start and end and selected_venues:
            # This will find any existing bookings that overlap in date and venue
            overlapping = BookingEnquiry.objects.filter(
                venues__in=selected_venues,
                start_date__lte=end,
                end_date__gte=start,
            ).exclude(pk=self.instance.pk).distinct()

            if overlapping.exists():
                conflict_names = ', '.join(set(v.name for b in overlapping for v in b.venues.all() if v in selected_venues))
                raise forms.ValidationError(
                    f"The following venues are already booked for this date range: {conflict_names}"
                )
