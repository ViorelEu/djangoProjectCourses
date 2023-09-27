from django import forms
from .models import Subscription


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = "__all__"

    # subscriptions = forms.ModelMultipleChoiceField(
    #     queryset=Subscription.objects.all(),
    #     widget=forms.CheckboxSelectMultiple()
    # )
