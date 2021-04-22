from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.
def student_show(request):
   student=Student.objects.order_by('roll_no')
   return render(request, 'student/student_show.html', {'student_list':student})
def setcookie(request):
    h = HttpResponse("<h1>Dataflair Django Tutorials</h1>")
    if request.COOKIES.get('visits'):
        h.set_cookie('dataflair', 'Welcome Back')
        value=int(request.COOKIES.get('visits'))
        h.set_cookie('visits', value+1)
    else:
        value=1
        text="Welcome for the first time"
        h.set_cookie('visits', value)
        h.set_cookie('dataflair', text)
    return h
        




def showcookie(request):
    show=request.COOKIES['dataflair']
    html="<h1>New Page</h1> <br><b>{0}</b>".format(show)
    return HttpResponse(html)