#Imports
from django.shortcuts import render
from django.http import HttpResponse

#dummy data
posts = [
	{
		'author': 'deanusjack',
		'title': 'Blog Post 1',
		'content': 'First Post Content',
		'date_posted': 'January 20th 2021'
	},
	{
		'author': 'deanusjack',
		'title': 'Blog Post 2',
		'content': 'Second Post Content',
		'date_posted': 'January 20th 2021'
	}
]

# Create your views here.
def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'main/home.html', context)

def about(request):
		return render(request, 'main/about.html')