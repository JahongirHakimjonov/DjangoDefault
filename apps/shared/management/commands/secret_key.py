from colorama import Fore, Style
from django.core.management import utils
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Generates a new Django secret key"

    def handle(self, *args, **options):
        print(
            Fore.LIGHTCYAN_EX
            + "<======================================================>"
        )
        print(
            "<=" + Style.RESET_ALL,
            Fore.LIGHTMAGENTA_EX + utils.get_random_secret_key() + Style.RESET_ALL,
            Fore.LIGHTCYAN_EX + "=>",
        )
        print(
            "<======================================================>" + Style.RESET_ALL
        )
