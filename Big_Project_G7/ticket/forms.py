from django import forms
from .models import *
from mysite.models import ExhibitionInfo
from django.utils import timezone
from datetime import timedelta

class TicketReservationForm(forms.ModelForm):
    exhibition_name = forms.ModelChoiceField(
        queryset=ExhibitionInfo.objects.filter(ExhibitionRegistrationDate__gt=timezone.now()),
        label="전시회 선택",
        widget=forms.Select(attrs={'class': 'form-control',}),
        empty_label= '전시회를 선택하세요.'
    )

    reservationDate = forms.ChoiceField(
        label="예약일",
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices= [(' ', '전시회를 먼저 선택하세요.')],
        required=True
    )

    class Meta:
        model = TicketBoughtInfo
        fields = ['exhibition_name', 'adult', 'child', 'reservationDate']
        labels = {
            'exhibition_name' : '전시회 명',
            'adult' : '성인',
            'child' : '청소년',
            'reservationDate' : '예약일'
        }
        widgets = {
            'adult' : forms.Select(choices=[(i, i) for i in range(10)], 
                                   attrs={'class': 'form-control','value':0}),
            'child' : forms.Select(choices=[(i, i) for i in range(10)],
                                   attrs={'class': 'form-control', 'value':0}),
        }
    
    def __init__(self, *args, **kwargs):
        reservationable_dates = kwargs.pop('reservationable_dates', None)
        super().__init__(*args, **kwargs)
        if reservationable_dates:
            self.fields['reservationDate'].choices = reservationable_dates

    def save(self, commit=True):
        reservation = super().save(commit=False)
        name = self.cleaned_data['exhibition_name']
        reservation.exhibitionid = ExhibitionInfo.objects.get(ExhibitionName=name).ExhibitionID

        if commit:
            reservation.save()
        return reservation