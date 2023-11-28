from django import forms

from .models import ConversationMessage

class ConverationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-6 py-4 rounded-xl border'
            }),
        }