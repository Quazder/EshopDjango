from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.core.validators import MinLengthValidator
from django.forms import Textarea

from Eshop.models import Recenze


class EditProfileForm(UserChangeForm):
    password = forms.CharField(label="", widget=forms.TextInput(attrs={'type': 'hidden'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emailova adresa'}))
    jmeno = forms.CharField(label="", max_length=100,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Jméno'}))
    prijmenu = forms.CharField(label="", max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Příjmení'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Uživatelské jméno'
        self.fields['username'].label = ''
        self.fields[
            'username'].help_text = '<span class="form-text text-muted"><small>MUsí obsahovat číslice a nebo ' \
                                    '@/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Heslo'
        self.fields['password1'].label = ''
        self.fields[
            'password1'].help_text = '<ul class="form-text text-muted small"><li>Vaše heslo by nemělo být stejné jako ' \
                                     'vaše ostatní hesla.</li><li>Heslo musí obsahovat aspoň 8 znaků</li><li>Heslo ' \
                                     'nesmí být jednoduché</li><li>Heslo nesmí obsahovat pouze čísla</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Potvrdit heslo'
        self.fields['password2'].label = ''
        self.fields[
            'password2'].help_text = '<span class="form-text text-muted"><small>Zadejte stejné heslo ' \
                                     'znovu</small></span>'


class RecenzeForm(forms.ModelForm):
    class Meta:
        model = Recenze
        fields = ['text']
        widgets = {
            'text': Textarea(attrs={'class': 'form-control review-textarea'}),
        }
        labels = {
            'text': 'Napište recenzi',
        }
        validators = {
            'text': MinLengthValidator(25, message="Recenze musí být alespoň 25 znaků dlouhá.")
        }
