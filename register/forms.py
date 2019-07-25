from django import forms

from .models import UserDetails

class UserForm(forms.ModelForm):
    image = forms.FileField()

    class Meta:
	    model = UserDetails
	    fields = '__all__'
	    widgets = {
            'password': forms.PasswordInput(),
        }
