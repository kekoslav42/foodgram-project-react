from django.http import HttpResponse

from .models import IngredientForRecipe


def get_send_file(recipes_list, filename):
    ingredients_dict = {}
    for recipe in recipes_list:
        ingredients = IngredientForRecipe.objects.filter(recipe=recipe.recipe)
        for ingredient in ingredients:
            name = ingredient.ingredient.name
            if name not in ingredients_dict:
                ingredients_dict[name] = {
                    'measurement_unit': ingredient.ingredient.measurement_unit,
                    'amount': ingredient.amount
                    }
            else:
                ingredients_dict[name]['amount'] += ingredient.amount
    buy_list = [
        f'{ingredient} - {ingredients_dict[ingredient]["amount"]} '
        f'{ingredients_dict[ingredient]["measurement_unit"]} \n'
        for ingredient in ingredients_dict
    ]
    response = HttpResponse(buy_list, 'Content-Type: text/plain')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response
