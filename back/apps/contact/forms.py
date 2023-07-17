#!/usr/bin/env python3

from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    name = forms.CharField(max_length=250)
    las_name = forms.CharField(max_length=250)
    messsage = forms.CharField(widget=forms.Textarea, required=True)
