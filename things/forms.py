"""Forms of the project."""
from django import forms
# Create your forms here.
class ThingForm(forms.Form):
    """Form of the project."""
    name = forms.CharField(label='Name', max_length=35, unique=True)
    description = forms.CharField(label='Description', max_length=120, blank=True)
    quantity = forms.IntegerField(label='Quantity', max=100, min=0)
