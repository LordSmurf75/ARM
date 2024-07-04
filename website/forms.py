from django import forms
from .models import Koncert, Spillested

class KoncertForm(forms.ModelForm):
    # Definer formfelter
    navn = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Navn'}),
        required=True
    )

    dato = forms.DateTimeField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dato: YYYY-MM-DD'}),
        required=True
    )

    spillested = forms.ModelChoiceField(
        queryset=Spillested.objects.all(),
        label="",
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Vælg et spillested",
        required=True
    )

    facebook = forms.URLField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Facebook URL'}),
        required=False
    )

    billetter = forms.URLField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Billet link'}),
        required=False
    )

    band1 = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Band 1'}),
        required=True
    )

    band2 = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Band 2'}),
        required=False
    )

    band3 = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Band 3'}),
        required=False
    )

    band4 = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Band 4'}),
        required=False
    )

    band5 = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Band 5'}),
        required=False
    )

    band6 = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Band 6'}),
        required=False
    )

    band7 = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Band 7'}),
        required=False
    )

    band8 = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Band 8'}),
        required=False
    )    

    offentliggjort = forms.BooleanField(
        label="Offentliggjort",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        initial=False,
        required=False
    )

    # Meta-klasse for model og felter
    class Meta:
        model = Koncert
        fields = ('navn', 'spillested', 'dato', 'facebook', 'billetter', 'band1', 'band2', 'band3', 'band4', 'band5', 'band6', 'band7', 'band8', 'offentliggjort')

    # Tilføj clean_spillested-metoden
    def clean_spillested(self):
        data = self.cleaned_data.get('spillested')
        # Hvis brugeren ikke har valgt et gyldigt spillested (empty_label), rejser vi en valideringsfejl
        if data is None:
            raise forms.ValidationError("Vælg venligst et gyldigt spillested.")
        # Returner det rensede data
        return data


class SpillestedForm(forms.ModelForm):
    # Definer formfelter
    navn = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Navn'}),
        required=True
    )

    adresse = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse'}),
        required=True
    )

    postnr = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postnummer'}),
        required=True
    )

    by = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'By'}),
        required=True
    )

    telefon = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefonnummer'}),
        required=False
    )

    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        required=True
    )

    hjemmeside = forms.URLField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hjemmeside'}),
        required=True
    )

    class Meta:
        model = Spillested
        fields = ('navn', 'adresse', 'postnr', 'by', 'telefon', 'email', 'hjemmeside')
