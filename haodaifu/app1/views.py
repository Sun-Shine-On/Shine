from django.shortcuts import render
from .models import answer

# Create your views here.
def index(request):
    alls = answer.objects.all()
    return render(request,'show.html',locals())


