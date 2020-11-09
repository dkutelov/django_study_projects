from django.shortcuts import render, redirect, get_object_or_404

from recipe.forms import RecipeForm, DeleteRecipeForm
from recipe.models import Recipe


def homepage(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == 'GET':
        form = RecipeForm(label_suffix='')
        return render(request, 'recipe/create.html', {'form': form})
    elif request.method == 'POST':
        form = RecipeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('homepage')

        return render(request, 'recipe/create.html', {'form': form})


def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == 'GET':
        form = RecipeForm(label_suffix='', instance=recipe)
        context = {
            'form': form,
            'recipe_id': recipe.id
        }
        return render(request, 'recipe/edit.html', context)

    elif request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)

        if form.is_valid():
            form.save()
            return redirect('homepage')

        context = {
            'form': form,
            'recipe_id': recipe.id
        }

        return render(request, 'recipe/edit.html', context)


def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == 'GET':
        form = DeleteRecipeForm(instance=recipe, label_suffix='')
        context = {
            'form': form,
            'recipe_id': recipe.id
        }
        return render(request, 'recipe/delete.html', context)
    elif request.method == 'POST':
        recipe.delete()
        return redirect('homepage')


def details_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    ingredients_list = recipe.ingredients.split(', ')
    context = {
        'recipe': recipe,
        'ingredients': ingredients_list
    }
    return render(request, 'recipe/details.html', context)