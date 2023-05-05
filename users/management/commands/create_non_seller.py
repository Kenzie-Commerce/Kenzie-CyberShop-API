from django.core.management.base import BaseCommand, CommandParser
from django.core.management import CommandError
from users.models import User


class Command(BaseCommand):
    help = "Create a user non seller"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "-u",
            "--username",
            type=str,
            help="Define a username",
        )
        parser.add_argument(
            "-p",
            "--password",
            type=str,
            help="Define a password",
        )
        parser.add_argument(
            "-e",
            "--email",
            type=str,
            help="Define a email",
        )

    def handle(self, *args: tuple, **kwargs: dict) -> str | None:
        username = kwargs.get("username") or "wigny"
        password = kwargs.get("password") or "1234"
        email = kwargs.get("email") or f"{username}@example.com"

        user_exists = User.objects.filter(username__iexact=username)
        email_exists = User.objects.filter(email__iexact=email)

        if user_exists:
            raise CommandError(f"Username `{username}` already taken.")
        elif email_exists:
            raise CommandError(f"Email `{email}` already taken.")
        else:
            User.objects.create_user(
                username=username,
                password=password,
                email=email,
            )
            return f"User Non Seller `{username}` successfully created!"
