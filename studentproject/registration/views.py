from django.shortcuts import render
from . import forms

#DataFlair #Form #View Functions
def regform(request):
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        html = 'we have recieved this form again'
        if form.is_valid():
            html=html+"The Form is Valid"
    else:
        html = 'welcome for first time'
    return render(request, 'registration/signup.html', {'html': html, 'form': form})