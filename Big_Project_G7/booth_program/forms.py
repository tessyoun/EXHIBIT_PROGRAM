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
    
    def save(self, commit=True, user=None):
        program = super().save(commit=False)
        if user:
            program.user = user
        if commit:
            program.save()
        return program


class ReservationForm(forms.ModelForm):
    program_name = forms.ChoiceField(
        label="프로그램 선택",
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_program_name'}),
        required=True,
    )

    reservationtime = forms.ChoiceField(
        label="예약 시간",
        widget=forms.Select(attrs={'class': 'form-control',  'id': 'id_reservationtime'}),
        choices= [('', '프로그램을 먼저 선택하세요.')],
        required=True
    )

    class Meta:
        model = BoothProgramReservation
        fields = ['program_name', 'num_of_people', 'reservationtime']

        labels = {
            'program_name' : '프로그램 명',
            'num_of_people' : '예약 인원',
            'reservationtime' : '예약 시간'
        } 

        widgets = {
            'num_of_people' : forms.Select(choices=[(i, i) for i in range(1, 10)], attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        programs = kwargs.pop('programs', None)
        reservation_time = kwargs.pop('reservation_times', [(' ', '프로그램을 먼저 선택하세요.')])
        super().__init__(*args, **kwargs)
        if programs:
            self.fields['program_name'].choices = [
                (program.id, program.name) for program in programs
            ]
            self.fields['program_name'].choices.insert(0,('','프로그램을 선택하세요.'))

        if reservation_time:
            self.fields['reservationtime'].choices = reservation_time

    def save(self, commit=True, user=None):
        reservation = super().save(commit=False)
        program_id = self.cleaned_data.get('program_name')
        if program_id:
            reservation.program = Program.objects.get(id=program_id)
        if user:
            reservation.user = user
        if commit:
            reservation.save()
        return reservation
