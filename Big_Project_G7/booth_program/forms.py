from django import forms
from django.contrib.auth.models import User
from .models import Program

class ProgramForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label="프로그램 명")
    description = forms.CharField(widget=forms.Textarea, label="프로그램 설명")
    selected_times = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Program
        fields = ['name', 'description', 'selected_times']