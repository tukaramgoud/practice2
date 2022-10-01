from django import forms
from .models import bank_dtl
class bank_form(forms.ModelForm):
    class Meta:
        model=bank_dtl
        fields='__all__'