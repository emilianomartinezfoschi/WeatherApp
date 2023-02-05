from django import forms

class Entrada(forms.Form):
    ciudad = forms.CharField(label="Ciudad", max_length=200,required=False, widget= forms.TextInput(
        attrs={
            'required':'True',
            'placeholder':'Ej. Mendoza, London, Paris, ó \'Rosario Santa Fe\'',
            'class':'mainform'
        }
    ))