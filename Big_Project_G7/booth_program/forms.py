from django import forms
from .models import Program, Booth

class ProgramForm(forms.ModelForm):
    booth_name = forms.CharField(max_length=100, label="프로그램 명")
    booth_description = forms.CharField(widget=forms.Textarea, label="프로그램 설명")

    class Meta:
        model = Program
        fields = ['booth_name', 'booth_description', 'name', 'description']
