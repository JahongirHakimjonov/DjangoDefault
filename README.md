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
bankai
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
- celery beat
- celery worker
- flower
- RabbitMQ
- Redis
- black
- pre-commit

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

# Donate
- [Buy Me Coffee](https://buymeacoffee.com/ja_khan_gir)

- [Tirikchilik](https://tirikchilik.uz/ja_khan_gir)


<a href="https://buymeacoffee.com/ja_khan_gir">
    <img src="https://i.postimg.cc/cLwdq9pL/bmc-qr-2.png" width="200" height="200" alt="pypi">
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

# Project Dependencies and Tools

This project utilizes a combination of powerful tools and technologies to manage background tasks, message queuing, and real-time monitoring. Below is an overview of the key components:

## Celery

Celery is an asynchronous task queue/job queue based on distributed message passing. It is focused on real-time operation but supports scheduling as well. The execution units, called tasks, are executed concurrently on one or more worker nodes using multiprocessing, Eventlet, or gevent. Celery is used in this project for handling background tasks efficiently.

### Key Components:

- **Celery Beat**: A scheduler for Celery. It kicks off tasks at regular intervals, which are then executed by available Celery workers. It's used for periodic tasks like cleaning up databases, sending emails, or gathering data from various sources.
- **Celery Worker**: These are the processes that run the actual tasks. A Celery system can have multiple workers, which can be located on the same machine or across a distributed network.

## RabbitMQ

RabbitMQ is an open-source message broker software that originally implemented the Advanced Message Queuing Protocol (AMQP). It facilitates the efficient delivery of messages in complex routing scenarios and ensures that messages are processed only once, in the order they are sent. In this project, RabbitMQ is used as the message broker for Celery, managing the queue of tasks to be processed by the workers.

## Redis

Redis is an in-memory data structure store, used as a database, cache, and message broker. In this project, Redis is used in two main roles:
- As a message broker, similar to RabbitMQ, offering support for fast, transient storage scenarios.
- For storing the task results (Celery supports using Redis as a result backend).

## Flower

Flower is a web-based tool for monitoring and administrating Celery clusters. It provides detailed real-time information about task queues, workers, and tasks, with the ability to control them directly through the web interface. Flower is an essential tool for managing and troubleshooting Celery tasks and workers in this project.

---

To set up these components for your development environment, refer to the respective official documentation for installation and configuration guidelines.

## General Information

These commands are designed to streamline common tasks in Django development and deployment. Ensure you have the necessary permissions and environment setup before running these commands.


## Pre-commit for Code Quality Assurance

Pre-commit is an essential tool in modern development workflows, ensuring that code committed to the repository adheres to defined quality standards. It automates the process of checking code for common issues before it is committed, helping to maintain a clean and error-free codebase.

### Features and Benefits:

- **Automated Code Review**: Runs a series of checks on code before it is committed, catching issues early in the development cycle.
- **Customizable Hooks**: Supports a wide range of hooks for different languages and frameworks, including Python and JavaScript, making it versatile for projects with diverse tech stacks.
- **Easy Integration**: Can be easily integrated into existing projects with minimal setup, enhancing the development process without significant overhead.

### Setting Up Pre-commit in Your Project:

1. **Installation**: Install pre-commit using pip:
   ```bash
   pip install pre-commit
   ```
2. **Configuration**: Create a `.pre-commit-config.yaml` file in your project root directory. Define the hooks you want to use, as shown in the project's current configuration.
3. **Install Git Hook Scripts**: Run the following command to set up pre-commit with your git hooks:
   ```bash
   pre-commit install
   ```
   This step ensures that pre-commit runs automatically on every commit attempt.

4. **Optional: Commit Message Hooks**: For projects requiring commit message standards, pre-commit can enforce this through commit message hooks:
   ```bash
   pre-commit install --hook-type commit-msg
   ```

5. **Manual Run**: To manually run pre-commit on all files in the project, use:
   ```bash
   pre-commit run --all-files
   ```
   This is useful for initial setup or periodic checks across the entire codebase.

### Example Configuration:

The project's `.pre-commit-config.yaml` includes hooks for checking JSON, TOML, and ensuring no merge conflicts, among others. It also utilizes `ruff` for fast Python linting and formatting, demonstrating the flexibility and power of pre-commit in maintaining code quality.

For detailed information and advanced configurations, refer to the [official pre-commit documentation](https://pre-commit.com/).



# Development
### Pre-commit
Before adding any source code, it is recommended to have pre-commit installed on your local computer to check for all potential issues when comitting the code.
```bash
black . # Format the code
pip install pre-commit
pre-commit install
pre-commit install --hook-type commit-msg
pre-commit run --all-files # Check if everything is okay
```

## Star History

<a href="https://www.star-history.com/#JahongirHakimjonov/DjangoDefault&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=JahongirHakimjonov/DjangoDefault&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=JahongirHakimjonov/DjangoDefault&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=JahongirHakimjonov/DjangoDefault&type=Date" />
 </picture>
</a>
