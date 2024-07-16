from django import forms
from .models import *
from exhibition.models import Exhibition_info
from django.utils import timezone
from datetime import timedelta

class TicketReservationForm(forms.ModelForm):
    exhibition_name = forms.ModelChoiceField(
        queryset=Exhibition_info.objects.filter(start_date__gt=timezone.now()),
        label="전시회 선택",
        widget=forms.Select(attrs={'class': 'form-control',}),
        empty_label= '전시회를 선택하세요.'
    )

    reservationDate = forms.ChoiceField(
        label="예약일",
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices= [(' ', '전시회를 먼저 선택하세요.')],
        required=False
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
            'adult' : forms.Select(choices=[(i, i) for i in range(10)], attrs={'class': 'form-control', 'value':0}),
            'child' : forms.Select(choices=[(i, i) for i in range(10)], attrs={'class': 'form-control', 'value':0}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['reservationDate'].required = False
        self.fields['reservationDate'].choices = self.get_reservation_dates()

    def get_reservation_dates(self):
        return [(' ', '전시회를 먼저 선택하세요.')]

    def clean_reservationDate(self):
        exhibition_name = self.cleaned_data.get('exhibition_name')
        reservation_date = self.cleaned_data.get('reservationDate')

        if exhibition_name and reservation_date and reservation_date != ' ':
            exhibition = Exhibition_info.objects.get(exhibition_name=exhibition_name)
            available_dates = dict(exhibition.get_available_reservation_dates())

            if reservation_date not in available_dates:
                raise forms.ValidationError("예약일이 유효하지 않습니다.")

        return reservation_date
    
    def save(self, commit=True):
        reservation = super(TicketBoughtInfo, self).save(commit=False)
        name = self.cleaned_data['exhibition_name']
        exhibition = Exhibition_info.objects.get(exhibition_name=name)
        reservation.exhibitionid = exhibition.exhibition_id
        reservation_date = self.data.get('reservationDate')
        if reservation_date:
            reservation.reservationDate = reservation_date

        if commit:
            reservation.save()
        return reservation