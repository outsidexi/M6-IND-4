from django import forms

class FormularioUsuarioForm(forms.Form):
    direccion = forms.CharField(max_length=50, label="Direccion", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su direccion'}))
    edad = forms.IntegerField(label="Edad", required=True, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Ingrese su edad'}))
    profesion = forms.CharField(max_length=50, label="Profesion", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su profesion'}))