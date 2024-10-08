from django.shortcuts import render, get_object_or_404
from Store.models import Movie
def home(request):
    movie=Movie.objects.all()
    top = Movie.objects.order_by('-views')[:5]
    return render(request,'index.html',{'movie':movie,'top':top})
def movies(request):
    search=''
    if request.method=="POST":
        search=request.POST['search']
        movies=Movie.objects.filter(title__icontains=search)
    else:
        movies=Movie.objects.filter(type='movie')
    return render(request,'movies.html',{'movies':movies,'search':search})
def tvshow(request):
    tvshow=Movie.objects.filter(type='TV Show')
    return render(request,'tvshow.html',{'tvshow':tvshow})
def show(request,pk):
    movie=get_object_or_404(Movie,pk=pk)
    session_key = f'viewed_page_{pk}'
    if not request.session.get(session_key, False):  # If the session doesn't have the key, it's a new view
        movie.views += 1
        movie.save()  # Save the incremented view count
        request.session[session_key] = True 
    top = Movie.objects.order_by('-views')[:5]
    return render(request,'show.html',{'movie':movie,'top':top})



    