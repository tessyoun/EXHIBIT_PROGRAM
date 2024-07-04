from django import forms
from .models import *

class ExhibitionForm(forms.ModelForm):
    class Meta:
        model = Exhibition
        fields = ['exhibition_name', 'hall', 'start_date', 'end_date', 'number_of_booths']
        labels = {
            'exhibition_name': '전시회명',
            'hall': '전시장',
            'start_date': '전시 시작 날짜',
            'end_date':'전시 종료 날짜',
            'number_of_booths':'생성할 부스 개수',
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
    def save(self, commit=True):
        exhibition = super().save(commit=False)
        if commit:
            exhibition.save()
        return exhibition
    
    
class BoothForm(forms.ModelForm):
    class Meta:
        model = Booth_Info
        fields = ['booth_id','booth_name','company_id','company_name', 'exhibition_id', 'booth_category', 'background', 'service']