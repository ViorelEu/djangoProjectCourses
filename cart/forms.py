# cart/forms.py

from django import forms

from cart.models import Order


class CartForm(forms.Form):
    course_id = forms.IntegerField(widget=forms.HiddenInput())
    action = forms.CharField(widget=forms.HiddenInput())

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = []
