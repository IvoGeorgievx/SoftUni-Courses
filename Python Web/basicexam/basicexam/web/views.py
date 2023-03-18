from django.shortcuts import render, redirect

from basicexam.web.forms import CreateProfileForm, CarCreateForm, EditCarForm, DeleteCarForm, EditProfileForm, \
    DeleteProfileForm
from basicexam.web.models import Profile, Car


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
    return render(request, 'index.html', context)


def catalogue(request):
    cars_count = Car.objects.count()
    context = {
        'cars': Car.objects.all(),
        'cars_count': cars_count,
    }
    return render(request, 'catalogue.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
    }
    return render(request, 'profile-create.html', context)


def car_create(request):
    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }
    return render(request, 'car-create.html', context)


def car_details(request, pk):
    car = Car.objects.filter(pk=pk).get()
    context = {
        'car': car,
    }

    return render(request, 'car-details.html', context)


def car_edit(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EditCarForm(instance=car)
    else:
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'car-edit.html', context)


def car_delete(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = DeleteCarForm(instance=car)
    else:
        form = DeleteCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'car-delete.html', context)


def profile_details(request):
    profile = get_profile()
    query_data = list(Car.objects.all().values('price'))

    current_sum = 0
    if query_data:
        for i in query_data:
            for _, value in i.items():
                current_sum += value
    if profile is not None and Car.objects.count() > 0:
        average_price = current_sum / Car.objects.count()
    else:
        average_price = 0

    context = {
        'profile': profile,
        'average_price': average_price,
    }
    return render(request, 'profile-details.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile-edit.html', context)


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
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile-delete.html', context)
