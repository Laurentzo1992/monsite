from django.shortcuts import render

def index(request):
	context = {}
	return render(request, 'vuneem/index.html', context)


def cv(request):
   context = {}
   return render(request, 'vuneem/cv.html', context)

# Create your views here.
