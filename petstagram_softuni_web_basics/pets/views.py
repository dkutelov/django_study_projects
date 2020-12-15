from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from common.forms import CommentForm
from common.models import Comment
from core.clean_up import clean_up_files
from pets.forms import CreatePetForm
from pets.models import Pet, Like


def list_pets(req):
    context = {
        'pets': Pet.objects.all()
    }
    return render(req, 'pets/pet_list.html', context)


def get_detail_context(req, pet):
    comments = pet.comment_set.all()
    return {
        'pet': pet,
        'form': CommentForm(),
        'can_delete': req.user == pet.user.user,
        'can_edit': req.user == pet.user.user,
        'can_like': req.user != pet.user.user,
        'can_comment': req.user != pet.user.user,
        'has_liked': pet.like_set.filter(user_id=req.user.userprofile.id).exists(),
    }


def show_pet_detail(req, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()

    if req.method == 'GET':
        return render(req, 'pets/pet_detail.html', get_detail_context(req, pet))

    elif req.method == 'POST':
        form = CommentForm(req.POST)
        if form.is_valid():
            comment = Comment(comment=form.cleaned_data['comment'])
            comment.pet = pet
            comment.user = req.user.userprofile  # do not link to profile but user
            comment.save()
            pet.comment_set.add(comment)
            pet.save()

        # new_comment = Comment(pet=pet, comment=req.POST['comment'])
        # new_comment.save()
        # pet.comment_set.add(new_comment)
        return redirect('pet_details', pet.id)


@login_required
def like_pet(req, pk):
    #checks if liked and dislikes
    like = Like.objects.filter(user_id=req.user.userprofile.id, pet_id=pk).first()
    if like:
        like.delete()
    else:
        pet = Pet.objects.get(pk=pk)
        # new_like = pet.like_set.create()
        like = Like(pet=pet, user=req.user.userprofile)
        like.save()
        pet.like_set.add(like)
        pet.save()
        return redirect('pet_details', pk)


def persist(req, pet, html_template, redirect_url):
    if req.method == 'GET':
        context = {
            'form': CreatePetForm(instance=pet)
        }
        return render(req, f'pets/{html_template}.html', context)

    elif req.method == 'POST':
        old_image = pet.image
        if old_image:
            clean_up_files(old_image.path)
        form = CreatePetForm(req.POST, req.FILES, instance=pet)

        if not form.is_valid():
            context = {
                'form': form
            }
            return render(req, f'pets/{html_template}.html', context)

        form.save()

        if 'edit' in req.path:
            return redirect(redirect_url, pet.id)
        return redirect(redirect_url)


@login_required
def create_pet(req):
    return persist(req, Pet(), 'pet_create', 'list_pets')

@login_required
def edit_pet(req, pk):
    pet = Pet.objects.get(pk=pk)
    return persist(req, pet, 'pet_edit', 'pet_details')


@login_required
#@require_user(model=Pet)
def delete_pet(req, pk):
    pet = Pet.objects.get(pk=pk)
    if pet.user.user != req.user:
        pass
    else:
        if req.method == 'GET':
            return render(req, 'pets/pet_delete.html', {
                'name': pet.name
            })

        elif req.method == 'POST':
            pet.delete()
            return redirect('list_pets')

