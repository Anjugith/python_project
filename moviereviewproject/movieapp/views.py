from django.shortcuts import render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db.models import Q
from addmovieapp.models import Movie
from .models import UserProfile

# Create your views here.
def login(request):
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

def registration(request):
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
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Id already taken')
                return redirect('registration')
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
            return redirect('registration')

    return render(request, 'registration.html')
# def registration(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         password = request.POST['password']
#         cpassword = request.POST['password1']
#         if password == cpassword:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, 'Username Taken')
#                 return redirect('registration')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request, 'Email Id already taken')
#                 return redirect('registration')
#             else:
#                 user = User.objects.create_user(username=username, password=password, first_name=first_name,
#                                                 last_name=last_name, email=email)
#                 user.save();
#                 return redirect('login')
#         else:
#             messages.info(request, 'password not matching')
#             return redirect('registration')
#         return redirect('/')
#     return render(request, 'registration.html')
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

def logout(request):
    auth.logout(request)
    return redirect('/')


def index(request):
    return redirect(request, 'index.html')


# Create your views here.
def SearchResult(request):
    movies = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        movies = Movie.objects.filter(Q(title__contains=query) | Q(desc__contains=query))
    return render(request, 'search.html', {'query': query, 'movies': movies})


