from django.db.models import Sum
from django.http import HttpResponse

from .models import IngredientForRecipe, Recipe, Purchase, Ingredient


def get_send_file(request, filename):
    """ файл для скачивания P.S костыль"""
    user = request.user
    recipes = Purchase.objects.filter(user=user).values('recipe')
    ingredients_id = Recipe.objects.filter(
        id__in=recipes
    ).values('ingredients')
    ingredients = Ingredient.objects.filter(id__in=ingredients_id)

    to_buy = []

    for ingredient in ingredients:
        amount = IngredientForRecipe.objects.filter(
            ingredient=ingredient,
            recipe__in=recipes,
        ).aggregate(total_amount=Sum('amount'))["total_amount"]
        to_buy.append(
            f'{ingredient.name}: {amount} {ingredient.measurement_unit}.'
        )
    response = HttpResponse(to_buy, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response
