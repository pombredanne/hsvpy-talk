from django import forms

from .models import Paragraph, Story

class ParagraphForm(forms.ModelForm):
    class Meta:
        model = Paragraph
        fields = ("text", )
        widgets = {"text": forms.Textarea(attrs={"autofocus": "on",}),}

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ("title", )
        widgets = {"title": forms.TextInput(attrs={"autofocus": "on",}),}
