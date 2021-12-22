from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Create admin'

    def handle(self, email, password, username='', first='', last=''):
        if not username and not password.strip():
            return 'Неверное имя пользователя или пароль'

        user = User(
            username=username,
            email=email,
            first_name=first,
            last_name=last
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
