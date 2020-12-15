from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import View, TemplateView

from pets.forms import CreatePetForm
from pets.models import Pet


class IndexView(View):
    def get(self, request):
        return render(request, 'cbv/index.html')

    def post(self, request):
        pass

    # def despatch(self, request, *args, **kwargs):
    #     pass  # restrict user groups

class IndexTemplateView(TemplateView):
    template_name = 'cbv/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Hi'
        context['pets'] = Pet.objects.all()
        return context


class PetsListView(ListView):
    template_name = 'cbv/index.html'
    model = Pet
    context_object_name = 'pets'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # returns the pet list
        context['title'] = 'Pets List'
        return context

    def dispatch(self, request, *args, **kwargs):
        if 'page_size' in request.GET:
            self.paginate_by = request.GET['page_size']
        return super().dispatch(request, *args, **kwargs)


class PetDetailsView(DetailView):
    model = Pet
    template_name = 'cbv/detial.html'
    context_object_name = 'pet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # returns the pet list
        pet = context['pet']
        context['title'] = f'{pet.name} - Pet Details'
        return context


class PetCreateView(CreateView):
    model = Pet
    template_name = 'cbv/create.html'
    form_class = CreatePetForm
    # fields = '__all__'
    success_url = reverse_lazy('index')  #if not reverse it expects a string
    # lazy evaluates when needed to be executed

