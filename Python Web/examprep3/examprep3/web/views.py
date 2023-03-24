from django.shortcuts import render, redirect

from examprep3.web.forms import AddBookForm, EditBookForm, EditProfileForm, DeleteProfileForm, BaseProfileForm
from examprep3.web.models import Profile, Book


def get_profile():
    try:
        return Profile.objects.get()
    except:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        return redirect('add profile')
    context = {
        'profile': profile,
        'books': Book.objects.all()
    }

    return render(request, 'home-with-profile.html', context)


def add_book(request):
    profile = get_profile()
    if request.method == 'GET':
        form = AddBookForm()
    else:
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'add-book.html', context)


def edit_book(request, pk):
    book = Book.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EditBookForm(instance=book)
    else:
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'edit-book.html', context)


def book_details(request, pk):
    profile = get_profile()
    book = Book.objects.filter(pk=pk).get()
    context = {
        'book': book,
        'profile': profile,
    }
    return render(request, 'book-details.html', context)


def profile(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = Profile.objects.get()
    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'delete-profile.html', context)


def add_profile(request):
    if request.method == 'GET':
        form = BaseProfileForm()
    else:
        form = BaseProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)
