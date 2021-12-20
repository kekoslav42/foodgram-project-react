from django.urls import include, path
from djoser import views

from users.views import FollowApiView, ListFollowViewSet

urlpatterns = [
    path(
        'auth/token/login/',
        views.TokenCreateView.as_view(), name='login'
    ),
    path(
        'auth/token/logout/',
        views.TokenDestroyView.as_view(), name='logout'
    ),
    # id заменил на pk просто потому что не люблю переназначивать методы
    # которые идут в чистом питоне. т.е не стал переназначивать id
    path(
        'users/<int:pk>/subscribe/',
        FollowApiView.as_view(), name='subscribe'
    ),
    path(
        'users/subscriptions/',
        ListFollowViewSet.as_view(), name='subscription'
    ),
    path(
        '', include('djoser.urls')
    ),
]
