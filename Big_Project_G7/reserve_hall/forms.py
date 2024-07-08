from django import forms
from .models import Reservation_hall

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation_hall
        fields = [
            'hall_name', 'company', 'contact_name', 'contact_position', 'phone_number', 'email',
            'event_scale', 'start_date', 'end_date'
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date and start_date > end_date:
            self.add_error('start_date', "시작 날짜는 끝나는 날짜보다 이전이어야 합니다.")
            self.add_error('end_date', "끝나는 날짜는 시작 날짜보다 이후이어야 합니다.")
