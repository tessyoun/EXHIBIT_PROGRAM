from django import forms
from django.contrib.auth.models import User
# from .models import UserProfile
from django.contrib.auth.models import Group
from .models import Profile
from django.contrib.auth.forms import UserCreationForm  

class SignupForm(UserCreationForm):
    user_type = forms.ChoiceField(label='회원구분', choices=Profile.USER_TYPE_CHOICES, required=True)
    name = forms.CharField(label='이름')
    phone_number = forms.CharField(label='전화번호')
    
    class Meta(UserCreationForm.Meta):
        # fields = UserCreationForm.Meta.fields + ('email',)
        fields = UserCreationForm.Meta.fields + ('user_type', 'name', 'phone_number')
        labels = {
            'username': '아이디',
        }

    def save(self, commit=True):
        user = super().save(commit=True)
        user_type = self.cleaned_data['user_type']
        if commit:
            user.save()
            Profile.objects.create(user=user,
                               user_type=user_type,
                               name=self.cleaned_data['name'],
                               phone_number=self.cleaned_data['phone_number'],
                               )
            try:
                group = Group.objects.get(name=user_type)
            except Group.DoesNotExist:
                # 그룹이 없을 경우, 기본 그룹을 설정하거나 예외 처리
                group = None  # 예외 처리 로직 추가
            if group:
                user.groups.add(group)
    
class RegularUserSignUpForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='이름')
    phone = forms.CharField(max_length=20, label='전화번호')
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        labels = {
            'username': '아이디',
            'password': '비밀번호',
            'email': '이메일 주소',
        }
        widgets = {
            'password': forms.PasswordInput(),
        }

class BusinessUserSignUpForm(forms.ModelForm):
    company_name = forms.CharField(max_length=100, label='기업명')
    phone = forms.CharField(max_length=20, label='전화번호')

    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        labels = {
            'username': '아이디',
            'password': '비밀번호',
            'email': '이메일 주소',
        }
        widgets = {
            'password': forms.PasswordInput(),
        }
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_type', 'name', 'phone_number']