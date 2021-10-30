from django import forms


class primaryForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    con_password=forms.CharField(widget=forms.PasswordInput)


