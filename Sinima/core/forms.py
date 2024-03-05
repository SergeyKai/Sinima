from django import forms


class FeedBackForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    massage = forms.CharField(widget=forms.Textarea())



# xhfv fvpn nuxv ypce


