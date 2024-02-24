# views.py
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .models import Movie, Category, Comment, UserProfile
from .forms import UserRegistrationForm, MovieForm, CommentForm, ReviewForm
from .models import Movie, Review


def index(request,):
    movie_list = Movie.objects.all()
    return render(request, 'index.html', {'movie_list': movie_list})

def register(request):
    # if request.method == 'POST':
    #     form = UserRegistrationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         auth_login(request, user)
    #         messages.success(request, 'Registration successful. Welcome!')
    #         return redirect('index.html')  # Replace 'home' with your home page URL
    # else:
    #     form = UserRegistrationForm()
    # return render(request, 'register.html', {'form': form})
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Id already taken')
                return redirect('register')
            else:
                # Create a new user
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save()

                # Create a UserProfile for the user
                UserProfile.objects.create(user=user, first_name=first_name, last_name=last_name, email=email)

                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')

    return render(request, 'register.html')
def login(request):
    # if request.method == 'POST':
    #     form = AuthenticationForm(request, data=request.POST)
    #     if form.is_valid():
    #         auth_login(request, form.get_user())
    #         return redirect('index.html')  # Replace 'home' with your home page URL
    # else:
    #     form = AuthenticationForm()
    # return render(request, 'login.html', {'form': form})
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalied Cridentials')
            return redirect('login')
    return render(request, 'login.html')
def users(request):
    movie = Movie.objects.all()
    context = {
        'user_movies': movie
    }
    return render(request, 'users.html', context)
def edit_profile(request):
    if request.method == 'POST':
        # Get the updated values from the form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        # Update the user model
        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        messages.success(request, 'Your profile was successfully updated!')
        return redirect('edit_profile')
    else:
        return render(request, 'edit.html')
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

# @login_required
# def add_movie(request):
#     if request.method == 'POST':
#         form = MovieForm(request.POST, request.FILES)
#         if form.is_valid():
#             movie = form.save(commit=False)
#             movie.user = request.user
#             movie.save()
#             messages.success(request, 'Movie added successfully!')
#             return redirect('movie_list')  # Replace 'movie_list' with your movie listing page URL
#     else:
#         form = MovieForm()
#     return render(request, 'movies/add_movie.html', {'form': form})
def update(request,id):

    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('movieapp:users', user_id=movie.user.id)

    return render(request, 'edit.html', {'form': form, 'movie': movie})
def detail(request,movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = Review.objects.filter(movie=movie)

    return render(request, "detail.html", {'movie': movie, 'reviews': reviews})
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
                return redirect('movieapp:detail', movie_id=movie.id)
        else:
            messages.error(request, 'You must be logged in to submit a review.')
            return redirect('/')
    else:
        form = ReviewForm()

    return render(request, 'review.html', {'form': form, 'movie': movie})
def SearchResult(request):
    movies = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        movies = Movie.objects.filter(Q(title__contains=query) | Q(desc__contains=query))
    return render(request, 'search.html', {'query': query, 'movies': movies})
# def movie_detail(request, movie_id):
#     movie = get_object_or_404(Movie, id=movie_id)
#     comments = Comment.objects.filter(movie=movie)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.user = request.user
#             comment.movie = movie
#             comment.save()
#             messages.success(request, 'Comment added successfully!')
#             return redirect('movie_detail', movie_id=movie_id)
#     else:
#         form = CommentForm()
#     return render(request, 'movies/movie_detail.html', {'movie': movie, 'comments': comments, 'form': form})
#
# def movie_list(request):
#     movies = Movie.objects.all()
#     return render(request, 'movies/movie_list.html', {'movies': movies})
#
#
# # movieapp/views.py
#
# from django.shortcuts import render, get_object_or_404
# from .models import Movie, Comment
# from .forms import CommentForm  # Assuming you have a CommentForm defined in forms.py
#
#
# def add_comment(request, movie_id):
#     movie = get_object_or_404(Movie, pk=movie_id)
#
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.movie = movie
#             comment.save()
#             # You may add a redirect or render a success page here
#     else:
#         form = CommentForm()
#
#     return render(request, 'add_comment.html', {'form': form, 'movie': movie})
#
