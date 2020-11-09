from django.urls import path, include

from recipe.views import homepage, create_recipe, delete_recipe, edit_recipe, details_recipe

urlpatterns = [
    path('', homepage, name="homepage"),
    path('create/', create_recipe, name="create recipe"),
    path('edit/<int:recipe_id>', edit_recipe, name="edit recipe"),
    path('delete/<int:recipe_id>', delete_recipe, name="delete recipe"),
    path('details/<int:recipe_id>', details_recipe, name="details recipe"),
]
