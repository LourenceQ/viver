from django import forms
from .models import Agendar

class AgendarForm(forms.ModelForm):
    class Meta:
        model = Agendar
        fields = ['nome','sobrenome','email','celular','observações']

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'sobrenome': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'cidade': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.TextInput(attrs={"class":"form-select"}),
            'celular': forms.TextInput(attrs={'class':'form-control'}),
            'observações': forms.Textarea(attrs={'class':'form-control','rows':5,'cols':5}),
        }
