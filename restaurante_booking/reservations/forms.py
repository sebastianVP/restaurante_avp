# definir el formulario para las reservas
from django import forms
from .models import Reservation
# utilizaremos la libreria crispy_forms para el formulario de reservas
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ReservationForm(forms.ModelForm):
    class Meta:
        model= Reservation
        fields = ['name','email','date','guests']
        widgets = {'date':forms.DateTimeInput(attrs={
            'type':'datetime-local',
            'placeholder':'YYYY-MM-DD HH:MM'
        }),
        }

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper= FormHelper()
        self.helper.form_method= 'post'
        self.helper.add_input(Submit('Submit','Reservar'))