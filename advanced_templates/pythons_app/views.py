from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import PythonCreateForm, FilterForm
from .models import Python


# Create your views here.
# def index(req):
#     pythons = Python.objects.all()
#     return render(req, 'index.html', {'pythons': pythons, 'page': 'index'})

def extract_filter_values(params):
    order = params['order'] if 'order' in params else FilterForm.ORDER_ASC
    text = params['text'] if 'text' in params else ''

    return {
        'order': order,
        'text': text,
    }


class IndexView(ListView):
    model = Python
    template_name = 'index.html'
    context_object_name = 'pythons'
    order_by_asc = True
    order_by = 'name'
    contains_text = ''

    def dispatch(self, request, *args, **kwargs):
        params = extract_filter_values(request.GET)
        # self.order_by_asc = params['order'] == FilterForm.ORDER_ASC
        self.order_by = params['order']
        self.contains_text = params['text']
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        order_by = 'name' if self.order_by == FilterForm.ORDER_ASC else '-name'
        result = self.model.objects.filter(name__icontains=self.contains_text).order_by(order_by)

        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = FilterForm(initial={
            'order': self.order_by,
            'text': self.contains_text
        })
        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['pythons'] = sorted(context['pythons'], key=lambda x: x.name, reverse=not self.order_by_asc)
    #     context['filter_form'] = FilterForm(initial={'order': self.order_by_asc})
    #     return context


def create(req):
    if req.method == 'GET':
        form = PythonCreateForm()
        return render(req, 'create.html', {'form': form, 'page': 'create'})
    else:
        form = PythonCreateForm(req.POST, req.FILES)
        if form.is_valid():
            python = form.save()
            python.save()
            return redirect('index')
        return render(req, 'create.html', {'form': form, 'page': 'create'})