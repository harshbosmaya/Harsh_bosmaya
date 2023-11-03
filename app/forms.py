from django import forms

class contactform(forms.Form):
    name = forms.CharField(label="Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'required': True}))
    email = forms.EmailField(label="Email ID", widget=forms.EmailInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Email ID', 'required': True}))
    notes = forms.CharField(label="Notes", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Notes'}))
