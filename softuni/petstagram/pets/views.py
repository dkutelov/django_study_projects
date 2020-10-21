from django.shortcuts import render, redirect

from common.forms import CommentForm
from common.models import Comment
from pets.forms import CreatePetForm
from pets.models import Pet, Like


def list_pets(req):
    context = {
        'pets': Pet.objects.all()
    }
    return render(req, 'pets/pet_list.html', context)


def get_detail_context(pet):
    comments = pet.comment_set.all()
    return {
        'pet': pet,
        'form': CommentForm(),
        'comments': [element.comment for element in comments]
    }


def show_pet_detail(req, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()

    if req.method == 'GET':
        return render(req, 'pets/pet_detail.html', get_detail_context(pet))

    elif req.method == 'POST':
        form = CommentForm(req.POST)
        new_comment = Comment(pet=pet, comment=req.POST['comment'])
        new_comment.save()
        pet.comment_set.add(new_comment)
        return render(req, 'pets/pet_detail.html', get_detail_context(pet))


def like_pet(req, pk):
    pet = Pet.objects.get(pk=pk)
    new_like = pet.like_set.create()
    # like = Like(pet=pet)
    # like.save()
    # pet.like_set.add(like)
    # pet.save()
    return redirect('pet_details', pk)


def persist(req, pet, html_template, redirect_url):
    if req.method == 'GET':
        context = {
            'form': CreatePetForm(instance=pet)
        }
        return render(req, f'pets/{html_template}.html', context)
    elif req.method == 'POST':
        form = CreatePetForm(req.POST, instance=pet)

        if not form.is_valid():
            context = {
                'form': form
            }
            return render(req, f'pets/{html_template}.html', context)

        pet.save()

        if 'edit' in req.path:
            return redirect(redirect_url, pet.id)
        return redirect(redirect_url)


def create_pet(req):
    return persist(req, Pet(), 'pet_create', 'list_pets')


def edit_pet(req, pk):
    pet = Pet.objects.get(pk=pk)
    return persist(req, pet, 'pet_edit', 'pet_details')


def delete_pet(req, pk):
    pet = Pet.objects.get(pk=pk)
    if req.method == 'GET':
        return render(req, 'pets/pet_delete.html', {
            'name': pet.name
        })

    elif req.method == 'POST':
        pet.delete()
        return redirect('list_pets')

