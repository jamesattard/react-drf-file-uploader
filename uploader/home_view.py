from django.shortcuts import render

def index(request):

  context = {
    }

  response = render(request, 'index.html', context)
  return response
