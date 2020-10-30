from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
	{
		'difficulty': 'hard',
		'trail_name': 'Devil\'s Hole',
		'description': 'What a trail...it\'s a slap!',
		'location': '35.92264 -81.88675'
	},
	{
		'difficulty': 'moderate',
		'trail_name': 'Looking Glass Rock Trail',
		'description': 'Makes your legs go \'wooooooooooooo\'',
		'location': '35.29084 -82.77646'
	}
]


def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):

	return render(request, 'blog/about.html', {'title':'About'})


