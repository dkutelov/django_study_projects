from django.shortcuts import render, redirect

from books.forms import BookForm
from books.models import Book


def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'books/index.html', context)


def persist(request, book, template_name):

    if request.method == 'GET':
        context = {
            'form': BookForm(instance=book)
        }
        return render(request, f'books/{template_name}.html', context)
    else:
        form = BookForm(request.POST, instance=book)

        if not form.is_valid():
            context = {
                'form': form,
                'errors': form.errors
            }
            return render(request, f'books/{template_name}.html', context)

        form.save()
        return redirect('book index')



def create(request):
    return persist(request, Book(), 'create')  #send empty book instance


def edit(request, pk):
    return persist(request, Book.objects.get(pk=pk), 'edit')

# def create(request):
#     if request.method == 'GET':
#         #return empty form
#         context = {
#             'form': BookForm()
#         }
#         return render(request, 'books/create.html', context)
#     else:
#         #save form
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('book index')
#
#         context = {
#             'form': form
#         }
#
#         return render(request, 'books/create.html', context)


# def edit(request, pk):
#     book = Book.objects.get(pk=pk)
#
#     if request.method == 'GET':
#         context = {
#             'form': BookForm(instance=book)
#         }
#         return render(request, 'books/create.html', context)
#     else:
#         form = BookForm(request.POST, instance=book)
#
#         if form.is_valid():
#             form.save()
#             return redirect('book index')
#
#         context = {
#             'form': form
#         }
#         return render(request, 'books/create.html', context)

