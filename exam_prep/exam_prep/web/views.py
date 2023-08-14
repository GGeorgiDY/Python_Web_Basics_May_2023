from django.shortcuts import render, redirect
from exam_prep.web.forms import ProfileCreateForm, AlbumCreateForm, AlbumEditForm, AlbumDeleteForm, ProfileDeleteForm
from exam_prep.web.models import Profile, Album


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    # тук, проверяваме дали има профил и ако няма да покаже add profile в index страницата
    profile = get_profile()
    if profile is None:
        return add_profile(request)

    context = {
        'albums': Album.objects.all(),  # върни ми всичките албуми които имам
    }

    return render(request, 'core/home-with-profile.html', context)


def details_album(request, pk):
    album = Album.objects.filter(pk=pk).get
    context = {
        'album': album,
    }
    return render(request, 'albums/album-details.html', context)


def add_album(request):
    if request.method == 'GET': # Създай празна форма - формата за да я върнем.
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)  # Значи нещо е пратено към формата - формата за да я създадем
        if form.is_valid():  # валидираме си я и в същото време си попюлейтваме clean data
            form.save()    # сейфаш
            return redirect('index')    # по условие казаха да се редиректва към същата страница

    # Ако е GET или формата не е валидна
    context = {
        'form': form,
    }
    return render(request, 'albums/add-album.html', context)


def edit_album(request, pk):
    album = Album.objects.filter(pk=pk).get()   # това го правим защото влизайки в тази страница, ние сме влезли да едитваме конкретен албум, който ще го вземем на база pk
    if request.method == 'GET': # Създай празна форма - формата за да я върнем.
        form = AlbumEditForm(instance=album)    # instance=album се слага, защото като влезем да едитваме този албум, ние ще искаме да се показват първоначално посочените имена, цени и други ст-сти за този албум. За да можем да ги вземем се пише това.
    else:
        form = AlbumEditForm(request.POST, instance=album)  # Значи нещо е пратено към формата - формата за да я създадем. Тук пак слагаме това за instance=album, защото така казваме да се променят нещата които са различни и идват от POST заявката.
        if form.is_valid():  # валидираме си я и в същото време си попюлейтваме clean data
            form.save()    # сейфаш
            return redirect('index')    # по условие казаха да се редиректва към home page-a

    # Ако е GET или формата не е валидна
    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'albums/edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.filter(pk=pk).get()   # това го правим защото влизайки в тази страница, ние сме влезли да едитваме конкретен албум, който ще го вземем на база pk
    if request.method == 'GET': # Създай празна форма - формата за да я върнем.
        form = AlbumDeleteForm(instance=album)    # instance=album се слага, защото като влезем да едитваме този албум, ние ще искаме да се показват първоначално посочените имена, цени и други ст-сти за този албум. За да можем да ги вземем се пише това.
    else:
        # Album.objects.filter(pk=pk).delete()    # Don't do it that way. Така прескачаме абсолютно всички проверки, които може да сложиме във формата. Най-правилно е да я изтрием през формата. Това означава да промениме начина по който save работи в една форма.
        form = AlbumDeleteForm(request.POST, instance=album)  # Значи нещо е пратено към формата - формата за да я създадем. Тук пак слагаме това за instance=album, защото така казваме да се променят нещата които са различни и идват от POST заявката.
        if form.is_valid():  # валидираме си я и в същото време си попюлейтваме clean data
            form.save()    # сейфаш
            return redirect('index')    # по условие казаха да се редиректва към home page-a

    # Ако е GET или формата не е валидна
    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'albums/delete-album.html', context)


def details_profile(request):
    profile = get_profile()
    albums_count = Album.objects.count()
    context = {
        'profile': profile,
        'albums_count': albums_count,
    }
    return render(request, 'profiles/profile-details.html', context)


def add_profile(request):
    if get_profile() is not None:
        return redirect('index')

    if request.method == 'GET': # Създай празна форма - формата за да я върнем.
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)  # Значи нещо е пратено към формата - формата за да я създадем
        if form.is_valid():  # валидираме си я и в същото време си попюлейтваме clean data
            form.save()    # сейфаш
            return redirect('index')    # по условие казаха да се редиректва към същата страница

    # Ако е GET или формата не е валидна
    context = {
        'form': form,
            'hide_nav_links': True,
    }

    return render(request, 'core/home-no-profile.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'GET':                         # Създай празна форма - формата за да я върнем.
        form = ProfileDeleteForm(instance=profile)      # instance=profile се слага, защото ние искаме като влезем трием профила, да можем да вземем всичко като информация за този профил
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)  # Значи нещо е пратено към формата - формата за да я създадем. Тук пак слагаме това за instance=album, защото така казваме да се променят нещата които са различни и идват от POST заявката.
        if form.is_valid():                             # валидираме си я и в същото време си попюлейтваме clean data
            form.save()                                 # сейфаш
            return redirect('index')                    # по условие казаха да се редиректва към home page-a

    # Ако е GET или формата не е валидна
    context = {
        'form': form,
    }

    return render(request, 'profiles/profile-delete.html', context)

