from django.shortcuts import render, redirect
from exam_june_2023.web.forms import ProfileCreateForm, FruitCreateForm, FruitEditForm, FruitDeleteForm, \
    ProfileEditForm, ProfileDeleteForm
from exam_june_2023.web.models import Profile, Fruit


# тук проверяваме дали имаме профил (ще върне профила) или не (ще върне None)
def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
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
    return render(request, 'core/index.html', context)


def dashboard_page(request):
    profile = get_profile()
    showing = True
    if profile is None:   # Ако нямаме профил
        showing = False

    fruits = Fruit.objects.all()

    context = {
        'fruits': fruits,
        'showing': showing,
    }
    return render(request, 'dashboard/dashboard.html', context)


def create_fruit(request):
    if request.method == 'GET':   # Създай празна форма - формата за да я върнем.
        form = FruitCreateForm()
    else:
        form = FruitCreateForm(request.POST)   # Значи нещо е пратено към формата - формата за да я създадем
        if form.is_valid():   # валидираме си я и в същото време си попюлейтваме clean data. Казваме, ако е валидна
            form.save()   # сейфаш
            return redirect('dashboard page')   # по условие казаха да се редиректва към същата страница

    # Ако е GET или формата не е валидна
    context = {
        'form': form,
    }
    return render(request, 'fruit/create-fruit.html', context)


def details_fruit(request, pk):
    profile = get_profile()
    showing = True
    if profile is None:   # Ако нямаме профил
        showing = False

    fruit = Fruit.objects.filter(pk=pk).get()
    context = {
        'fruit': fruit,
        'showing': showing,
    }
    return render(request, 'fruit/details-fruit.html', context)


def edit_fruit(request, pk):
    profile = get_profile()
    showing = True
    if profile is None:   # Ако нямаме профил
        showing = False

    fruit = Fruit.objects.filter(pk=pk).get()
    if request.method == 'GET':   # Създай празна форма - формата за да я върнем.
        form = FruitEditForm(instance=fruit)    # instance=album се слага, защото като влезем да едитваме този албум, ние ще искаме да се показват първоначално посочените имена, цени и други ст-сти за този албум. За да можем да ги вземем се пише това.
    else:
        form = FruitEditForm(request.POST, instance=fruit)  # Значи нещо е пратено към формата - формата за да я създадем. Тук пак слагаме това за instance=album, защото така казваме да се променят нещата които са различни и идват от POST заявката.
        if form.is_valid():  # валидираме си я и в същото време си попюлейтваме clean data
            form.save()    # сейфаш
            return redirect('dashboard page')    # по условие казаха да се редиректва към home page-a

    # Ако е GET или формата не е валидна
    context = {
        'form': form,
        'fruit': fruit,
        'showing': showing,
    }

    return render(request, 'fruit/edit-fruit.html', context)


def delete_fruit(request, pk):
    profile = get_profile()
    showing = True
    if profile is None:   # Ако нямаме профил
        showing = False

    fruit = Fruit.objects.filter(pk=pk).get()

    if request.method == 'GET': # Създай празна форма - формата за да я върнем.
        form = FruitDeleteForm(instance=fruit)    # instance=album се слага, защото като влезем да едитваме този албум, ние ще искаме да се показват първоначално посочените имена, цени и други ст-сти за този албум. За да можем да ги вземем се пише това.
    else:
        # Album.objects.filter(pk=pk).delete()    # Don't do it that way. Така прескачаме абсолютно всички проверки, които може да сложиме във формата. Най-правилно е да я изтрием през формата. Това означава да промениме начина по който save работи в една форма.
        form = FruitDeleteForm(request.POST, instance=fruit)  # Значи нещо е пратено към формата - формата за да я създадем. Тук пак слагаме това за instance=album, защото така казваме да се променят нещата които са различни и идват от POST заявката.
        if form.is_valid():  # валидираме си я и в същото време си попюлейтваме clean data
            form.save()    # сейфаш
            return redirect('dashboard page')    # по условие казаха да се редиректва към home page-a

    # Ако е GET или формата не е валидна
    context = {
        'form': form,
        'fruit': fruit,
        'showing': showing,
    }
    return render(request, 'fruit/delete-fruit.html', context)


def create_profile(request):
    # ако имаме профил но цъкнем на profile/add, да не ни дава да си добавяме профил, а да ни редиректва към index страницата
    if get_profile() is not None:
        return redirect('index')

    if request.method == 'GET':   # Създай празна форма - формата за да я върнем.
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)   # Значи нещо е пратено към формата - формата за да я създадем
        if form.is_valid():   # валидираме си я и в същото време си попюлейтваме clean data. Казваме, ако е валидна
            form.save()   # сейфаш
            return redirect('dashboard page')   # по условие казаха да се редиректва към същата страница

    # Ако е GET или формата не е валидна
    context = {
        'form': form,
    }
    return render(request, 'profile/create-profile.html', context)


def details_profile(request):
    profile = get_profile()
    showing = True
    if profile is None:   # Ако нямаме профил
        showing = False

    profile = Profile.objects.get()
    fruits_count = Fruit.objects.count()
    context = {
        'profile': profile,
        'showing': showing,
        'fruits_count': fruits_count,
    }

    return render(request, 'profile/details-profile.html', context)


def edit_profile(request):
    profile = get_profile()
    showing = True
    if profile is None:   # Ако нямаме профил
        showing = False

    profile = Profile.objects.get()

    if request.method == 'GET':   # Създай празна форма - формата за да я върнем.
        form = ProfileEditForm(instance=profile)    # instance=album се слага, защото като влезем да едитваме този албум, ние ще искаме да се показват първоначално посочените имена, цени и други ст-сти за този албум. За да можем да ги вземем се пише това.
    else:
        form = ProfileEditForm(request.POST, instance=profile)  # Значи нещо е пратено към формата - формата за да я създадем. Тук пак слагаме това за instance=album, защото така казваме да се променят нещата които са различни и идват от POST заявката.
        if form.is_valid():  # валидираме си я и в същото време си попюлейтваме clean data
            form.save()    # сейфаш
            return redirect('dashboard page')    # по условие казаха да се редиректва към home page-a

    # Ако е GET или формата не е валидна
    context = {
        'form': form,
        'profile': profile,
        'showing': showing,
    }

    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    showing = True
    if profile is None:   # Ако нямаме профил
        showing = False

    profile = Profile.objects.get()
    print(profile)

    if request.method == 'GET':   # Създай празна форма - формата за да я върнем.
        form = ProfileDeleteForm(instance=profile)    # instance=album се слага, защото като влезем да едитваме този албум, ние ще искаме да се показват първоначално посочените имена, цени и други ст-сти за този албум. За да можем да ги вземем се пише това.
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)  # Значи нещо е пратено към формата - формата за да я създадем. Тук пак слагаме това за instance=album, защото така казваме да се променят нещата които са различни и идват от POST заявката.
        if form.is_valid():  # валидираме си я и в същото време си попюлейтваме clean data
            form.save()    # сейфаш
            return redirect('index')    # по условие казаха да се редиректва към home page-a

    # Ако е GET или формата не е валидна
    context = {
        'form': form,
        'profile': profile,
        'showing': showing,
    }
    return render(request, 'profile/delete-profile.html', context)
