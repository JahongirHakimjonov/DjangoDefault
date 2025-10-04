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

        init_file_path = os.path.join("apps", "__init__.py")

        if not os.path.exists(init_file_path):
            open(init_file_path, "w").close()

        call_command("startapp", app_name, app_directory)

        apps_file_path = os.path.join(app_directory, "apps.py")
        with open(apps_file_path, "r") as file:
            filedata = file.read()

        filedata = filedata.replace(f'name = "{app_name}"', f'name = "apps.{app_name}"')

        with open(apps_file_path, "w") as file:
            file.write(filedata)

        for file_name in ["admin.py", "models.py", "views.py", "tests.py"]:
            os.remove(os.path.join(app_directory, file_name))

        urls_file_path = os.path.join(app_directory, "urls.py")
        with open(urls_file_path, "w") as file:
            file.write("from django.urls import path\n\nurlpatterns = []\n")

        def create_package(package_name):
            os.makedirs(package_name, exist_ok=True)
            with open(os.path.join(package_name, "__init__.py"), "w"):
                pass

        init_code = """
        import importlib\nimport os\n\ncurrent_dir = os.path.dirname(__file__)\n\nfor filename in os.listdir(current_dir):\n\tif filename.endswith(".py") and filename != "__init__.py":\n\t\tmodule_name = f"{__name__}.{filename[:-3]}"\n\t\timportlib.import_module(module_name)
        """

        for package_name in ["models", "views", "admin", "serializers", "tests"]:
            create_package(os.path.join(app_directory, package_name))
            with open(
                os.path.join(app_directory, package_name, "__init__.py"), "w"
            ) as file:
                file.write(init_code.strip())

        self.stdout.write(self.style.SUCCESS(f"App {app_name} created successfully!"))
