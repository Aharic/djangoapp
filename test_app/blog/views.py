from django.shortcuts import render
from .models import trails, gear


def home(request):
	context = {
		'trails': trails.objects.all()
	}
	return render(request, 'blog/home.html', context)

def about(request):

	return render(request, 'blog/about.html', {'title':'About'})


