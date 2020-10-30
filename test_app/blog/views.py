from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
trails = [
	{
		'difficulty': '5',
		'trail_name': 'Devil\'s Hole',
		'description': 'What a trail...it\'s a slap!',
		'location': '35.92264 -81.88675'
	},
	{
		'difficulty': '3',
		'trail_name': 'Looking Glass Trail',
		'description': 'You love to camp on it',
		'location': '34.80636 -82.32582'
	}
]


def home(request):
	context = {
		'trails': trails
	}
	return render(request, 'blog/home.html', context)

def about(request):

	return render(request, 'blog/about.html', {'title':'About'})


