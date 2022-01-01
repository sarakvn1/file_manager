from django import forms

class FileForm(forms.Form):
    video = forms.FileField()