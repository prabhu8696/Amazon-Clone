from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Enter Password',
        'class'       : 'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Confirm Password'
    }))


    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password', 'confirm_password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        passworld = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if passworld != confirm_password:
            raise forms.ValidationError(
                "Password does not match"
            )