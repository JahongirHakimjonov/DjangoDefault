import os

from colorama import Fore, Style
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Generates a new nginx config file with custom domain and project path"

    def handle(self, *args, **kwargs):
        domain_name = input(
            Fore.LIGHTCYAN_EX + "Please enter the domain name: " + Style.RESET_ALL
        )
        project_name = input(
            Fore.LIGHTMAGENTA_EX + "\nPlease enter the project name: " + Style.RESET_ALL
        )
        project_port = input(
            Fore.LIGHTBLUE_EX + "\nPlease enter the project port: " + Style.RESET_ALL
        )

        source_file_path = "./deployments/compose/nginx/nginx.conf"
        target_dir_path = "./deployments/nginx"
        target_file_path = f"{target_dir_path}/{domain_name}.conf"

        with open(source_file_path, "r") as file:
            file_contents = file.read()

        file_contents = file_contents.replace("yourdomain.uz", domain_name)
        file_contents = file_contents.replace("/path/project", project_name)
        file_contents = file_contents.replace("PROJECT_PORT", project_port)

        os.makedirs(target_dir_path, exist_ok=True)

        with open(target_file_path, "w") as file:
            file.write(file_contents)

        self.stdout.write(
            self.style.SUCCESS(
                Fore.LIGHTGREEN_EX
                + f"\n\n\nSuccessfully created {target_file_path}\n\n"
                + Style.RESET_ALL
            )
        )
