from django.shortcuts import render, redirect

from exprepsix.web.forms import CreateProfileForm, CreateGameForm, EditGameForm, DeleteGameForm, EditProfileForm, \
    DeleteProfileForm
from exprepsix.web.models import Profile, GameModel


def get_profile():
    try:
        return Profile.objects.get()
    except:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        return redirect('create profile')
    context = {
        'profile': profile,
    }

    return render(request, 'home-page.html', context)


def dashboard(request):
    context = {
        'games': GameModel.objects.all()
    }
    return render(request, 'dashboard.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'create-profile.html', context)


def details_profile(request):
    games = GameModel.objects.count()
    current_sum = 0
    average_rating = list(GameModel.objects.all().values('rating'))
    if average_rating:
        for i in average_rating:
            for _, value in i.items():
                current_sum += value
    if games > 0:
        average_total = current_sum / games
    else:
        average_total = 0

    context = {
        'profile': Profile.objects.get(),
        'games': games,
        'average': average_total,
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
            return redirect('details profile')
    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.get()
    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'delete-profile.html', context)


def create_game(request):
    if request.method == 'GET':
        form = CreateGameForm()
    else:
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form,
    }
    return render(request, 'create-game.html', context)


def details_game(request, pk):
    game = GameModel.objects.filter(pk=pk).get()
    context = {
        'game': game,
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
        'game': game,
        'form': form,
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
        'game': game,
        'form': form,
    }
    return render(request, 'delete-game.html', context)
