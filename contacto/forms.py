from django import forms

class FormularioContacto(forms.Form):

    nombre=forms.CharField(label="Nombre", required=True)
    cargo=forms.CharField(label="Cargo", required=True)
    email=forms.EmailField(label="Email", required=True)
    contenido=forms.CharField(label="Contenido", required=True, widget=forms.Textarea)
