from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render, redirect
from . models import Movie
from . forms import MovieForm,ReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    movie_list =Movie.objects.all()  # This line is causing the error
    return render(request, 'index.html', {'movie_list': movie_list})
    # movie_list=Movie.objects.all()
    # context={
    #     'movie_list':movie
    # }
    # return render(request,'index.html', context)
def detail(request,movie_id):
    # movie = get_object_or_404(Movie, id=movie_id)
    movie=Movie.objects.get(id=movie_id)
    # reviews = movie.review_set.all()
    return render(request,"detail.html",{'movie':movie})
def add_movie(request):
    # movie_list = Movie.objects.all()
    if request.method=="POST":
        title=request.POST.get('title')
        desc = request.POST.get('desc')
        release_date = request.POST.get('release_date')
        actors=request.POST.get('actors')
        category=request.POST.get('category')
        trailer_link=request.POST.get('trailer_link')
        poster = request.FILES['poster']
        user_rating = request.POST.get('user_rating')
        user_review = request.POST.get('user_review')
        movie=Movie(title=title,desc=desc,release_date=release_date,actors=actors,category=category,
                    trailer_link=trailer_link,poster=poster,user_rating=user_rating,user_review=user_review)
        movie.save()
        messages.success(request, 'Your profile was successfully Created!')
        return redirect('/')
    return render(request,'add.html')
    # if request.method == "POST":
    #     form = MovieForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/')
    # else:
    #     form = MovieForm()
    #
    # return render(request, 'add.html', {'form': form})
def update(request,id):
    # movie=Movie.objects.get(id=id)
    # form=MovieForm(request.POST or None,request.FILES,instance=movie)
    # if form.is_valid():
    #     form.save()
    #     return redirect('/')
    # return render(request,'edit.html',{'form':form,'movie':movie})
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('addmovieapp:users', user_id=movie.user.id)

    return render(request, 'edit.html', {'form': form, 'movie': movie})
def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
def users(request):
    movie = Movie.objects.all()
    context = {
        'user_movies': movie
    }
    return render(request, 'users.html', context)
# @login_required
def add_review(request,movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    # movie = Movie.objects.get(id=movie_id)
    # movie = get_object_or_404(Movie, id=movie_id)

    if request.method == "POST":
        if request.user.is_authenticated:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.movie = movie
                review.save()
                return redirect('addmovieapp:detail', movie_id=movie.id)
        else:
            messages.error(request, 'You must be logged in to submit a review.')
            return redirect('/')
    else:
        form = ReviewForm()

    return render(request, 'review.html', {'form': form, 'movie': movie})
            # movie.user_rating = form.cleaned_data['user_rating']
            # movie.user_review = form.cleaned_data['user_review']
            # movie.save()
    #         return redirect('detail', movie_id=movie.id)
    #
    # else:
    #     form = ReviewForm()
    #
    # return render(request, 'review.html', {'form': form, 'movie': movie})
