from django import forms
from .models import Program

class ProgramForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label="프로그램 명")
    description = forms.CharField(widget=forms.Textarea, label="프로그램 설명")
    selected_times = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Program
        fields = ['name', 'description', 'selected_times']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ProgramForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['company_name'] = forms.CharField(initial=user.profile.name, widget=forms.HiddenInput(), required=False)
