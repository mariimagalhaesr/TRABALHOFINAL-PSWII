from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Administrador

class AdministradorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Administrador
        fields = ('username', 'email')

class AdministradorChangeForm(UserChangeForm):
    class Meta:
        model = Administrador
        fields = ('username', 'email')