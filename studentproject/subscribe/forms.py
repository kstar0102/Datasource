from django import forms
class Subscribe(forms.Form):
    Email = forms.EmailField()
    subject=forms.CharField(max_length=100)
    message=forms.CharField(max_length=500)
    
    def __str__(self):
        return self.Email
