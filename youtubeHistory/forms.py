from django import forms

class HistoryEntryForm(forms.Form):
    url = forms.CharField(max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Video URL'}))
    annotation = forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Annotation\nExample: cool video to show my friends'}), required=False)