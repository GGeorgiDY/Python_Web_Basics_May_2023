from django.shortcuts import render, redirect

from final_exam.web.forms import ProfileCreateForm, EventCreateForm, EventEditForm, EventDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from final_exam.web.models import ProfileModel, EventModel


def get_profile():
    try:
        return ProfileModel.objects.get()
    except ProfileModel.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()
    showing = True
    if profile is None:   # Ако нямаме профил
        showing = False

    context = {
        'profile': profile,
        'showing': showing,
    }
    return render(request, 'shared/home-page.html', context)


def dashboard_page(request):
    profile = get_profile()
    showing = True
    if profile is None:   # Ако нямаме профил
        showing = False

    events = EventModel.objects.all()

    context = {
        'events': events,
        'showing': showing,
    }
    return render(request, 'events/dashboard.html', context)


def create_event(request):
    profile = get_profile()
    showing = True
    if profile is None:   # Ако нямаме профил
        showing = False

    if request.method == 'GET':
        form = EventCreateForm()
    else:
        form = EventCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        'form': form,
        'showing': showing,
    }
    return render(request, 'events/event-create.html', context)


def details_event(request, pk):
    profile = get_profile()
    showing = True
    if profile is None:   # Ако нямаме профил
        showing = False

    event = EventModel.objects.filter(pk=pk).get()
    context = {
        'event': event,
        'showing': showing,
    }
    return render(request, 'events/events-details.html', context)


def edit_event(request, pk):
    profile = get_profile()
    showing = True
    if profile is None:   # Ако нямаме профил
        showing = False

    event = EventModel.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EventEditForm(instance=event)
    else:
        form = EventEditForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        'form': form,
        'event': event,
        'showing': showing,
    }
    return render(request, 'events/event-edit.html', context)


def delete_event(request, pk):
    profile = get_profile()
    showing = True
    if profile is None:   # Ако нямаме профил
        showing = False

    event = EventModel.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = EventDeleteForm(instance=event)
    else:
        form = EventDeleteForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        'form': form,
        'event': event,
        'showing': showing,
    }
    return render(request, 'events/events-delete.html', context)


def create_profile(request):
    if get_profile() is not None:
        return redirect('index')

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    # Ако е GET или формата не е валидна
    context = {
        'form': form,
    }
    return render(request, 'profiles/profile-create.html', context)


def details_profile(request):
    profile = get_profile()
    showing = True
    if profile is None:   # Ако нямаме профил
        showing = False

    profile = ProfileModel.objects.get()
    events_count = EventModel.objects.count()
    context = {
        'profile': profile,
        'showing': showing,
        'events_count': events_count,
    }

    return render(request, 'profiles/profile-details.html', context)


def edit_profile(request):
    profile = get_profile()
    showing = True
    if profile is None:   # Ако нямаме профил
        showing = False

    profile = ProfileModel.objects.get()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
        'profile': profile,
        'showing': showing,
    }

    return render(request, 'profiles/profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()
    showing = True
    if profile is None:   # Ако нямаме профил
        showing = False

    profile = ProfileModel.objects.get()

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
        'showing': showing,
    }
    return render(request, 'profiles/profile-delete.html', context)
