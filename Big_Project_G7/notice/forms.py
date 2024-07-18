from django import forms
from .models import Notice
from django.core.exceptions import ValidationError
import os

def file_extension_validator(file):
    valid_extension = ['.pdf', '.zip' ,'.jpg', '.jpeg', '.png']
    extension = os.path.splitext(file.name)[1]
    if extension not in valid_extension:
        raise ValidationError('pdf, zip, png, jpg, jpeg 파일만 업로드 가능합니다.')

class NoticeForm(forms.ModelForm):
    upload_files = forms.FileField(
        required=False,
        validators = [file_extension_validator]
    )

    class Meta:
        model = Notice
        fields = ['title', 'content', 'upload_files']
    
    def clean_upload_files(self):
        file = self.cleaned_data.get('upload_files', False)
        if file:
            file_extension_validator(file)
        return file