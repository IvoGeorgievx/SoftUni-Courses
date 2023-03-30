from django.shortcuts import render, redirect

from epfour.web.forms import ProfileCreateForm, NoteCreateForm, EditNoteForm, DeleteNoteForm, ProfileDeleteForm
from epfour.web.models import Profile, Note


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
        'notes': Note.objects.all()
    }
    return render(request, 'home-with-profile.html', context)


def add_note(request):
    if request.method == 'GET':
        form = NoteCreateForm()
    else:
        form = NoteCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EditNoteForm(instance=note)
    else:
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = DeleteNoteForm(instance=note)
    else:
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'note-delete.html', context)


def details_note(request, pk):
    note = Note.objects.filter(pk=pk).get()
    context = {
        'note': note,
    }
    return render(request, 'note-details.html', context)


def profile(request):
    profile = get_profile()
    notes = Note.objects.count()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('index')
    context = {
        'form': form,
        'profile': profile,
        'notes': notes,
    }
    return render(request, 'profile.html', context)


def create_profile(request):

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)
