from django import forms
from .models import Program

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
        elif len(selected_times.split(',')) > 1:
            self.add_error('selected_times', "시간대는 하나만 선택할 수 있습니다.")
