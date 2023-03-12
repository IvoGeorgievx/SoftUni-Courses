from django.shortcuts import render, redirect
from django.db.models import Avg, Sum

from exam_first_prep.gamesplay_app.models import GameModel, Profile, CreateProfileForm, CreateGameForm, EditGameForm, \
    DeleteGameForm, EditProfileForm, DeleteProfileForm


def get_profile():
    try:
        return Profile.objects.get()
    except:
        return None


def home_page(request):
    profile = get_profile()
    if profile is None:
        redirect('home page')

    context = {
        'profile': profile
    }
    return render(request, 'home-page.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form
    }

    return render(request, 'create-profile.html', context)


def dashboard(request):
    context = {
        'games': GameModel.objects.all()
    }
    return render(request, 'dashboard.html', context)


def create_game(request):
    if request.method == 'GET':
        form = CreateGameForm()
    else:
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form
    }
    return render(request, 'create-game.html', context)


def details_game(request, pk):
    current_game = GameModel.objects.filter(pk=pk).get()
    context = {
        'game_details': current_game
    }
    return render(request, 'details-game.html', context)


def edit_game(request, pk):
    game = GameModel.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EditGameForm(instance=game)
    else:
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'game': game
    }
    return render(request, 'edit-game.html', context)


def delete_game(request, pk):
    game = GameModel.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = DeleteGameForm(instance=game)
    else:
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'game': game
    }
    return render(request, 'delete-game.html', context)


def details_profile(request):
    profile = Profile.objects.get()
    games = GameModel.objects.count()
    context = {
        'profile': profile,
        'games': games,
    }

    return render(request, 'details-profile.html', context)


def edit_profile(request):
    profile = Profile.objects.get()
    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    profile = Profile.objects.get()
    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'delete-profile.html', context)
