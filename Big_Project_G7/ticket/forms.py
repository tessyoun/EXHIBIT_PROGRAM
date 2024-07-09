from django import forms
from .models import *
from exhibition.models import Exhibition_info
from django.utils import timezone

class TicketReservationForm(forms.ModelForm):
    exhibition_name = forms.ModelChoiceField(
        queryset=Exhibition_info.objects.filter(start_date__gt=timezone.now()),
        label="전시회 선택",
        widget=forms.Select(attrs={'class': 'form-control'}),
        to_field_name='exhibition_name'
    )

    class Meta:
        model = TicketBoughtInfo
        fields = ['exhibition_name']

    def save(self, commit=True):
        reservation = super().save(commit=False)
        name = self.cleaned_data['exhibition_name']
        exhibition = Exhibition_info.objects.get(exhibition_name=name)
        reservation.exhibitionid = exhibition.exhibition_id
        if commit:
            reservation.save()
        return reservation