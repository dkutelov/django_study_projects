from django.shortcuts import render, redirect
from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.generic import ListView, UpdateView, DetailView, DeleteView,CreateView
from animals.forms import AnimalForm
from animals.models import Animal, Owner


def serialized_data(data):
    try:
        return serialize('json', data)
    except TypeError:
        return serialize('json', [data])


def all_animals(req):
    animals = Animal.objects.all()
    context = {
        'animals': animals
    }
    return render(req, "animals/animal_list.html", context)


def all_animals_json(req):
    name = req.GET.get('name')
    if name:
        animal = Animal.objects.filter(name=name)
        return HttpResponse(serialized_data(animal))
    else:
        animals = Animal.objects.order_by('-age')
        return HttpResponse(serialized_data(animals))


def all_dogs(req):
    dogs = Animal.objects.filter(kind='D')
    context = {
        'animals': dogs
    }
    return render(req, "animals/index.html", context)


def all_cats(req):
    cats = Animal.objects.filter(kind='C')
    context = {
        'animals': cats
    }
    return render(req, "animals/index.html", context)


def animal_by_id(req, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    context = {
        'animal': animal
    }
    return render(req, "animals/animal.html", context)


def animal_by_id_json(req, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    return HttpResponse(serialized_data(animal))


def create_animal(req):
    if req.method == 'GET':
        context = {'form': AnimalForm()}
        return render(req, 'animals/animal_create.html', context)
    elif req.method == 'POST':
        form = AnimalForm(req.POST)

        if not form.is_valid():
            return render(req, 'animals/animal_create.html', {'form': AnimalForm(), 'error': form.errors})

        new_animal = form.save(commit=False)
        new_animal.owner = Owner.objects.get(pk=1)
        new_animal.save()
        return redirect('allanimals')


# class views

class AnimalList(ListView):
    model = Animal
    template_name = 'animals/animal_list.html'

    def get_context_object_name(self, object_list):
        return 'animals'


class AnimalCreate(CreateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'animals/animal_create.html'
    success_url = '/animals/class-all/'


class AnimalUpdate(UpdateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'animals/animal_create.html'
    success_url = '/animals/class-all/'


class AnimalDetail(DetailView):
    model = Animal
    template_name = 'animals/animal_detail.html'


class AnimalDelete(DeleteView):
    model = Animal
    template_name = 'animals/animal_delete.html'
    success_url = '/animals/class-all/'

