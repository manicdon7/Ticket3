from django import forms

class EventForm(forms.Form):
    event_name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    date = forms.DateField()
    location = forms.CharField(max_length=100)
    seats = forms.IntegerField()
    price = forms.DecimalField(decimal_places=2)
