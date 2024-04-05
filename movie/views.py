from django.shortcuts import render
from . models import Movies

# Create your views here.
def create(request):
    if request.POST:
        print(request.POST)
        
        title=request.POST.get('title')
        year=request.POST.get('year')
        description=request.POST.get('summary')

        movie=Movies(title=title, year=year, description=description)
        movie.save()

    return render(request, 'create.html')

def list(request):
    movie_data = Movies.objects.all()
    print(movie_data, request)
    return render(request, 'list.html', {'movies':movie_data})

def edit(request):
    return render(request, 'edit.html')