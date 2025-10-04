import os
from typing import Any

from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates a new Django app inside the apps folder and sets the name in apps.py"

    def add_arguments(self, parser: Any) -> None:
        parser.add_argument("app_name", type=str, help="The name of the app to create")
        return None

    def handle(self, *args: Any, **options: Any) -> None:
        app_name = options["app_name"]
        app_directory = os.path.join("apps", app_name)
        os.makedirs(app_directory, exist_ok=True)

        init_file_path = os.path.join("apps", "__init__.py")
        if not os.path.exists(init_file_path):
            open(init_file_path, "w").close()

        call_command("startapp", app_name, app_directory)

        # Fix apps.py name
        apps_file_path = os.path.join(app_directory, "apps.py")
        with open(apps_file_path, encoding="utf-8") as f:
            data = f.read()
        data = data.replace(f"name = '{app_name}'", f'name = "apps.{app_name}"')
        with open(apps_file_path, "w", encoding="utf-8") as f:
            f.write(data)

        # Remove default single-file modules
        for file_name in ["admin.py", "models.py", "views.py", "tests.py"]:
            path = os.path.join(app_directory, file_name)
            if os.path.exists(path):
                os.remove(path)

        # Create urls.py
        urls_file_path = os.path.join(app_directory, "urls.py")
        if not os.path.exists(urls_file_path):
            with open(urls_file_path, "w", encoding="utf-8") as f:
                f.write("from django.urls import path\n\nurlpatterns = []\n")

        def ensure_package(dir_path: str) -> None:
            os.makedirs(dir_path, exist_ok=True)
            init_path = os.path.join(dir_path, "__init__.py")
            if not os.path.exists(init_path):
                with open(init_path, "w", encoding="utf-8"):
                    pass

        # Autoload init code for root-level grouped modules
        init_code = (
            "import importlib\n"
            "import os\n\n"
            "current_dir = os.path.dirname(__file__)\n\n"
            "for filename in os.listdir(current_dir):\n"
            "\tif filename.endswith('.py') and filename != '__init__.py':\n"
            '\t\tmodule_name = f"{__name__}.{filename[:-3]}"\n'
            "\t\timportlib.import_module(module_name)"
        )

        # Root-level packages
        for pkg in ["models", "admin"]:
            pkg_path = os.path.join(app_directory, pkg)
            ensure_package(pkg_path)
            with open(os.path.join(pkg_path, "__init__.py"), "w", encoding="utf-8") as f:
                f.write(init_code)

        # api/v1 structure
        api_base = os.path.join(app_directory, "api")
        v1_base = os.path.join(api_base, "v1")
        ensure_package(api_base)
        ensure_package(v1_base)

        for sub in ["views", "serializers", "tests"]:
            sub_path = os.path.join(v1_base, sub)
            ensure_package(sub_path)

        # Optionally aggregate imports at api/v1/__init__.py
        v1_init = os.path.join(v1_base, "__init__.py")
        with open(v1_init, "w", encoding="utf-8") as f:
            f.write("from . import views, serializers, tests  # noqa\n")

        self.stdout.write(self.style.SUCCESS(f"App {app_name} created successfully!"))
        return None
