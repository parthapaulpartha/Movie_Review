from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    slider_images, movie_reviews, comment_movie_review
)

from .forms import (
    RegistrationForm,
    LoginForm,
    EditprofileForm,
    CommentMovieReviewForm,
    ContactForm,
)

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import (
        authenticate,
        login,
        logout,
        update_session_auth_hash,
)

from django.db.models import Q
from django.contrib import messages


# Create your views here.
# -------- Registration ------
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success! Your account signup successfully')
            return redirect('movie_review/ragistration')

        else:
            messages.error(request, 'Please enter currenct informations')
            return redirect('movie_review/registration')

    else:
        form = RegistrationForm()
        arg = {'form': form}
    return render(request, 'movie_reviewapp/registration.html', arg)

# -------- Login ------
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if not user:
                messages.error(request, 'Username and Password did not matched')
                return redirect('/movie_review/login')
            login(request, user)
            return redirect('/movie_review/home/')
    else:
        form = LoginForm()
        arg = {'form': form}
    return render(request, 'movie_reviewapp/login.html', arg)

# -------- Logout ------
def logout_view(request):
    logout(request)
    return redirect('/movie_review/login/')

# ------ Profile ---------
def profile(request):
    return render(request, 'movie_reviewapp/profile.html')

# ------- Edit Profile -------
def edit_profile(request):
    if request.method == 'POST':
        form_u = EditprofileForm(request.POST, instance=request.user)
        if form_u.is_valid():
            form_u.save()
            messages.success(request, 'Profile Update successfully')
            return redirect('/movie_review/profile/')
    else:
        form_u = EditprofileForm(instance=request.user)
        arg = {'form_u': form_u}
    return render(request, 'movie_reviewapp/edit_profile.html', arg)

# -------- Change Password ---------
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password Change Successfully')
            return redirect('/movie_review/profile')
        else:
            messages.error(request, 'Did not match')
            return redirect('/movie_review/change_password')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'movie_reviewapp/change_password.html', args)

# -------- home -----
def home(request):
    all_images = slider_images.objects.all()
    all_movie_review = movie_reviews.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.name = request.user
            instance.save()
            return redirect('movie_review/home/')
    else:
        form = ContactForm()

    args = {
        'images': all_images,
        'movie_review': all_movie_review,
        'form': form
            }
    return render(request, 'movie_reviewapp/home.html', args)

# ---------- search post -------
def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        if search:
            match = movie_reviews.objects.filter(Q(movie_name__icontains=search))

            if match:
                return render(request, 'movie_reviewapp/search.html', {'sr': match})
            else:
                messages.error(request, 'No result found')
        else:
            return redirect('/movie_review/search')

    return render(request, 'movie_reviewapp/search.html')

def movie_list(request):
    movies = movie_reviews.objects.all()
    args = {
        'movie': movies,
    }
    return render(request, 'movie_reviewapp/movie_list.html', args)

def movie_detail(request, id, movie_name):
    movie_info = movie_reviews.objects.filter(id=id, movie_name=movie_name)
    movie = get_object_or_404(movie_reviews, id=id)
    getcomment = comment_movie_review.objects.filter(post=id)
    if request.method == 'POST':
        form = CommentMovieReviewForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.post = movie
            instance.name = request.user
            instance.save()
            return redirect('/movie_review/movie_list/')
    else:
        form = CommentMovieReviewForm()
    args = {
        'movie_info': movie_info,
        'getcomment': getcomment,
        'form': form,

    }
    return render(request, 'movie_reviewapp/movie_detail.html', args)

# -------- About us -------
def about_us(request):
    return render(request, 'movie_reviewapp/about_us.html')