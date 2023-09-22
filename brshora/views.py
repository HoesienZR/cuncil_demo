from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Statue
# Create your views here.
def brstatueview(request):
    statues=Statue.objects.all()
    context={
        'statues':statues,
                           }
    return render(request,'brshora/brshora.html',context=context)