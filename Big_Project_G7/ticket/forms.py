from django import forms
from .models import *
from exhibition.models import Exhibition_info
from django.utils import timezone

class TicketReservationForm(forms.ModelForm):
    exhibition_name = forms.ModelChoiceField(
        queryset=Exhibition_info.objects.filter(start_date__gt=timezone.now()),
        label="전시회 선택",
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label= '전시회를 선택하세요.'
    )

    date = forms.ChoiceField(
        label="예약일",
        widget=forms.Select(choices= [], attrs={'class': 'form-control'}),
    )

    class Meta:
        model = TicketBoughtInfo
        fields = ['exhibition_name', 'adult', 'child', 'date']
        labels = {
            'exhibition_name' : '전시회 명',
            'adult' : '성인',
            'child' : '청소년',
            'date' : '예약일'
        }
        widgets = {
            'adult' : forms.Select(choices=[(i, i) for i in range(10)], attrs={'class': 'form-control', 'value':0}),
            'child' : forms.Select(choices=[(i, i) for i in range(10)], attrs={'class': 'form-control', 'value':0}),
        }

    def save(self, commit=True):
        reservation = super().save(commit=False)
        name = self.cleaned_data['exhibition_name']
        exhibition = Exhibition_info.objects.get(exhibition_name=name)
        reservation.exhibitionid = exhibition.exhibition_id
        if commit:
            reservation.save()
        return reservation