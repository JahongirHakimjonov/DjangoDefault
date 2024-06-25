import os

from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = (
        "Creates a new Django app inside the apps folder and sets the name in apps.py"
    )

    def add_arguments(self, parser):
        parser.add_argument("app_name", type=str, help="The name of the app to create")

    def handle(self, *args, **options):
        app_name = options["app_name"]
        app_directory = os.path.join("apps", app_name)

        os.makedirs(app_directory, exist_ok=True)

        call_command("startapp", app_name, app_directory)

        apps_file_path = os.path.join(app_directory, "apps.py")
        with open(apps_file_path, "r") as file:
            filedata = file.read()

        filedata = filedata.replace(f'name = "{app_name}"', f'name = "apps.{app_name}"')

        with open(apps_file_path, "w") as file:
            file.write(filedata)

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created app "{app_name}" inside the apps folder and updated apps.py'
            )
        )
