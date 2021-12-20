from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from foodgram import custom_filters, custom_permissions, pagination

from .mixins import ListAndRetrieveSet
from .models import Favorite, Ingredient, Purchase, Recipe, Tag
from .serializers import (CreateRecipeSerializer, FavouriteSerializer,
                          IngredientSerializer, PurchaseSerializer,
                          ReadyRecipeSerializer, TagSerializer)
from .services import get_send_file


class TagsViewSet(ListAndRetrieveSet):
    """ Вьюсет для тегов (Миксин) """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None


class IngredientsViewSet(ListAndRetrieveSet):
    """ Вьюсет для ингредиентов (Миксин) """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = custom_filters.IngredientsFilter
    pagination_class = None


class RecipeViewSet(viewsets.ModelViewSet):
    """ Вьюсет для рецептов/фаворитов/списка покупок """
    queryset = Recipe.objects.all().order_by('-id')
    permission_classes = [
        permissions.AllowAny
    ]
    filter_backends = [DjangoFilterBackend]
    filterset_class = custom_filters.RecipeFilter
    pagination_class = pagination.CustomPageNumberPaginator

    def get_serializer_class(self):
        """ Выбор сериализатора """
        return (
            ReadyRecipeSerializer if self.request.method == 'GET' else
            CreateRecipeSerializer
        )

    @action(
        detail=True,
        methods=['POST', ],
        permission_classes=[custom_permissions.IsAuthorOrAdmin]
    )
    def favorite(self, request, pk):
        """ Добавление избранных рецептов"""
        data = {'user': request.user.id, 'recipe': pk}
        serializer = FavouriteSerializer(
            data=data, context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @favorite.mapping.delete
    def delete_favorite(self, request, pk):
        """ Удаление избранных рецептов """
        get_object_or_404(
            Favorite,
            user=request.user,
            recipe=get_object_or_404(Recipe, id=pk)
        ).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(
        detail=True,
        methods=['POST', ],
        permission_classes=[custom_permissions.IsAuthorOrAdmin]
    )
    def shopping_cart(self, request, pk):
        """ Добавление шоппинг карты"""
        data = {'user': request.user.id, 'recipe': pk}
        serializer = PurchaseSerializer(
            data=data, context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @shopping_cart.mapping.delete
    def delete_shopping_cart(self, request, pk):
        """ Удаление шоппинг карты """
        get_object_or_404(
            Purchase,
            user=request.user,
            recipe=get_object_or_404(Recipe, id=pk)
        ).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, permission_classes=[permissions.IsAuthenticated])
    def download_shopping_cart(self, request):
        """ Скачивание списка покупок """
        return get_send_file(
            request.user.purchase.all(), f'Список покупок: {request.user}.txt'
        )
