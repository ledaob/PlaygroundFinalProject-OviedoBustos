from django import forms


from .models import User_profile

class UserEditForm(forms.ModelForm):
    password = None
    correo = forms.EmailField()
    apellido = forms.CharField()
    nombre= forms.CharField()

    class Meta:
        model = User_profile
        fields = ['nombre','apellido', 'correo']

