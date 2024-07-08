# Django Default

![banner](https://i.postimg.cc/WzS3fs9f/Pics-Art-24-07-08-01-10-45-321.png "banner")

Django Default is a Django project structure generator that simplifies the process of setting up new Django projects. It automates the cloning of a predefined Django project structure from a GitHub repository, enabling developers to start their projects with a solid foundation.

## Features

- Automates the cloning of a Django project structure.
- Customizable to fit specific project needs.
- Streamlines the initial setup process for Django projects.

## Installation

Install Django Default using pip:

```bash
pip install django-default
```

## Usage

To generate a new Django project structure, execute the following command:

```bash
shinzo
```

This command clones the predefined Django project structure into your current working directory.

## Configuration

After generating your project structure, configure it by setting up the database and adjusting the settings in `settings.py` to match your environment. Ensure to include the third-party apps listed in `core/config/apps.py`:

- jazzmin
- modeltranslation
- django_ckeditor_5
- corsheaders
- rosetta
- rest_framework
- drf_spectacular
- drf_spectacular_sidecar

## Development

To contribute to Django Default, set up a development environment by cloning the project and installing its dependencies. Run tests to ensure your changes don't break existing functionality and follow the project's contribution guidelines when submitting pull requests.

## API Documentation

If your project uses Django REST Framework, use `drf_spectacular` to auto-generate API documentation. Document your API endpoints, including information on request methods, parameters, and example responses.

## License

Django Default is released under the MIT License. See the LICENSE file in the project repository for more information.

## Acknowledgments

- Thanks to all contributors who have helped to improve Django Default.
- Special thanks to Jahongir Hakimjonov for creating and maintaining this project.

## Contact

Please contact Jahongir Hakimjonov with any questions or concerns regarding this project.

- [GitHub](https://github.com/JahongirHakimjonov)
- [Instagram](https://www.instagram.com/ja_kahn_gir/)
- [Telegram](https://t.me/jakhangir_blog)

<a href="https://pypi.org/project/django-default/">
    <img src="https://i0.wp.com/securityaffairs.com/wp-content/uploads/2021/08/PyPI.png?ssl=1" width="200" height="90" alt="pypi">
</a>

# Management Commands Documentation

This document provides an overview and usage instructions for custom management commands included in the Django project.

## Commands

### createadmin

- **Description**: Creates superuser accounts with predefined credentials. Useful for quickly setting up admin users during development.
- **Usage**: `python manage.py createadmin`

### makeapp

- **Description**: Automates the creation of a new Django app within the `apps` directory. It also modifies the app's `apps.py` to correctly reference the app's location and removes unnecessary files.
- **Usage**: `python manage.py makeapp <app_name>`
  - `<app_name>`: The name of the app you want to create.

### nginx

- **Description**: Generates a new nginx configuration file based on user input for domain name, project name, and project port. The command simplifies the process of preparing nginx for new projects.
- **Usage**: `python manage.py nginx`
  - Follow the prompts to enter the domain name, project name, and project port.

### secret_key

- **Description**: Generates a new Django secret key. This is particularly useful when setting up a new project or when you need to regenerate the secret key for security reasons.
- **Usage**: `python manage.py secret_key`

## General Information

These commands are designed to streamline common tasks in Django development and deployment. Ensure you have the necessary permissions and environment setup before running these commands.


# Development
### Pre-commit
Before adding any source code, it is recommended to have pre-commit installed on your local computer to check for all potential issues when comitting the code.
```bash
pip install pre-commit
pre-commit install
pre-commit install --hook-type commit-msg
pre-commit run --all-files # Check if everything is okay
```
