from django.shortcuts import render, redirect
from final_exam_2023.web.forms import ProfileCreateForm, FruitCreateForm, FruitEditForm, FruitDeleteForm, \
    ProfileEditForm, ProfileDeleteForm
from final_exam_2023.web.models import ProfileModel, FruitModel


def get_profile():
    try:
        return ProfileModel.objects.get()
    except ProfileModel.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        if_profile = False
    else:
        if_profile = True

    context = {
        'if_profile': if_profile,
    }
    return render(request, 'core/../../templates/index.html', context)


def dashboard_page(request):
    profile = get_profile()
    fruits_count = FruitModel.objects.count()
    if profile is None:
        if_profile = False
    else:
        if_profile = True

    context = {
        'fruits': FruitModel.objects.all(),  # върни ми всичките плодове които имам
        'if_profile': if_profile,
        'fruits_count': fruits_count,
    }

    return render(request, 'core/dashboard.html', context)


def create_fruit(request):
    profile = get_profile()
    if profile is None:
        if_profile = False
    else:
        if_profile = True

    if request.method == 'GET':                 # Създай празна форма - формата за да я върнем.
        form = FruitCreateForm()
    else:
        form = FruitCreateForm(request.POST)    # Значи нещо е пратено към формата - формата за да я създадем
        if form.is_valid():                     # валидираме си я и в същото време си попюлейтваме clean data
            form.save()                         # сейфаш
            return redirect('dashboard page')   # по условие казаха да се редиректва към същата страница

    # Ако е GET или формата не е валидна
    context = {
        'form': form,
        'if_profile': if_profile,
    }
    return render(request, 'fruits/create-fruit.html', context)


def details_fruit(request, pk):
    profile = get_profile()
    if profile is None:
        if_profile = False
    else:
        if_profile = True

    fruit = FruitModel.objects.filter(pk=pk).get()
    context = {
        'fruit': fruit,
        'if_profile': if_profile,
    }
    return render(request, 'fruits/details-fruit.html', context)


def edit_fruit(request, pk):
    profile = get_profile()
    if profile is None:
        if_profile = False
    else:
        if_profile = True

    fruit = FruitModel.objects.filter(pk=pk).get()          # това го правим защото влизайки в тази страница, ние сме влезли да едитваме конкретен албум, който ще го вземем на база pk
    if request.method == 'GET':                             # Създай празна форма - формата за да я върнем.
        form = FruitEditForm(instance=fruit)                # instance=album се слага, защото като влезем да едитваме този албум, ние ще искаме да се показват първоначално посочените имена, цени и други ст-сти за този албум. За да можем да ги вземем се пише това.
    else:
        form = FruitEditForm(request.POST, instance=fruit)  # Значи нещо е пратено към формата - формата за да я създадем. Тук пак слагаме това за instance=album, защото така казваме да се променят нещата които са различни и идват от POST заявката.
        if form.is_valid():                                 # валидираме си я и в същото време си попюлейтваме clean data
            form.save()                                     # сейфаш
            return redirect('dashboard page')                        # по условие казаха да се редиректва към home page-a

    # Ако е GET или формата не е валидна
    context = {
        'form': form,
        'fruit': fruit,
        'if_profile': if_profile,
    }
    return render(request, 'fruits/edit-fruit.html', context)


def delete_fruit(request, pk):
    profile = get_profile()
    if profile is None:
        if_profile = False
    else:
        if_profile = True

    fruit = FruitModel.objects.filter(pk=pk).get()              # това го правим защото влизайки в тази страница, ние сме влезли да едитваме конкретен албум, който ще го вземем на база pk
    if request.method == 'GET':                                 # Създай празна форма - формата за да я върнем.
        form = FruitDeleteForm(instance=fruit)                  # instance=album се слага, защото като влезем да едитваме този албум, ние ще искаме да се показват първоначално посочените имена, цени и други ст-сти за този албум. За да можем да ги вземем се пише това.
    else:
        # Album.objects.filter(pk=pk).delete()                  # Don't do it that way. Така прескачаме абсолютно всички проверки, които може да сложиме във формата. Най-правилно е да я изтрием през формата. Това означава да промениме начина по който save работи в една форма.
        form = FruitDeleteForm(request.POST, instance=fruit)    # Значи нещо е пратено към формата - формата за да я създадем. Тук пак слагаме това за instance=album, защото така казваме да се променят нещата които са различни и идват от POST заявката.
        if form.is_valid():                                     # валидираме си я и в същото време си попюлейтваме clean data
            form.save()                                         # сейфаш
            return redirect('dashboard page')                   # по условие казаха да се редиректва към home page-a

    # Ако е GET или формата не е валидна
    context = {
        'form': form,
        'fruit': fruit,
        'if_profile': if_profile,
    }
    return render(request, 'fruits/delete-fruit.html', context)


def create_profile(request):
    if request.method == 'GET':                 # Създай празна форма - формата за да я върнем.
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)  # Значи нещо е пратено към формата - формата за да я създадем
        if form.is_valid():                     # валидираме си я и в същото време си попюлейтваме clean data
            form.save()                         # сейфаш
            return redirect('dashboard page')   # по условие казаха да се редиректва към същата страница

    # Ако е GET или формата не е валидна
    context = {
        'form': form,
    }

    return render(request, 'profiles/create-profile.html', context)


def details_profile(request):
    profile = get_profile()
    if profile is None:
        if_profile = False
    else:
        if_profile = True

    posts_count = FruitModel.objects.count()
    context = {
        'profile': profile,
        'posts_count': posts_count,
        'if_profile': if_profile,
    }

    return render(request, 'profiles/details-profile.html', context)


def edit_profile(request):
    profile = ProfileModel.objects.get()
    if profile is None:
        if_profile = False
    else:
        if_profile = True

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    # Ако е GET или формата не е валидна
    context = {
        'form': form,
        'profile': profile,
        'if_profile': if_profile,
    }

    return render(request, 'profiles/edit-profile.html', context)


def delete_profile(request):
    profile = ProfileModel.objects.get()
    if profile is None:
        if_profile = False
    else:
        if_profile = True

    if request.method == 'GET':                                     # Създай празна форма - формата за да я върнем.
        form = ProfileDeleteForm(instance=profile)                  # instance=profile се слага, защото ние искаме като влезем трием профила, да можем да вземем всичко като информация за този профил
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)    # Значи нещо е пратено към формата - формата за да я създадем. Тук пак слагаме това за instance=album, защото така казваме да се променят нещата които са различни и идват от POST заявката.
        if form.is_valid():                                         # валидираме си я и в същото време си попюлейтваме clean data
            # profile.objects.delete()
            form.save()                                             # сейфаш
            return redirect('index')                                # по условие казаха да се редиректва към home page-a

    # Ако е GET или формата не е валидна
    context = {
        'form': form,
        'if_profile': if_profile,
    }
    return render(request, 'profiles/delete-profile.html', context)