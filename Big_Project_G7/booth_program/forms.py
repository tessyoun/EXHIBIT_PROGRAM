from django import forms
from django.contrib.auth.models import User
from .models import Program, BoothProgramReservation

class ProgramForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label="프로그램 명")
    description = forms.CharField(widget=forms.Textarea, label="프로그램 설명")
    selected_times = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Program
        fields = ['name', 'description', 'selected_times']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")
        selected_times = cleaned_data.get("selected_times")

        if not name:
            self.add_error('name', "프로그램 명을 입력해주세요.")
        if not description:
            self.add_error('description', "프로그램 설명을 입력해주세요.")
        if not selected_times:
            self.add_error('selected_times', "오픈할 시간대를 선택해주세요.")


class ReservationForm(forms.ModelForm):
    class Meta:
        model = BoothProgramReservation
        fields = ['num_of_people']
