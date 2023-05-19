# GradePro
## Installation

 - Clone or [download](https://github.com/ArthurAugustinho/GradePro/archive/refs/heads/main.zip) this repository;

 - Change directory to the projects folder and create a virtual environment;
  - On `\GradePro-repo`
    - `python -m venv venv_GradePro`
    - Activate the venv
      - `.\venv_GradePro\Scripts\activate`

- Install the dependencies;
  - On `\GradePro-repo`
    - `pip install pillow`
    - `pip install django`

- Run initial management commands

  - On `\GradePro-repo`
    - Create the database Migrations
      - `python .\manage.py makemigrations` 
    - Run the Migrations
      - `python .\manage.py migrate`
    - Collect Static Files
      - `python .\manage.py collectstatic --noinput`
    - Load the theme
      - `python .\manage.py loaddata`

- Create a Super User for testing
  - On `\GradePro-repo`
    - ` python .\manage.py createsuperuser` 

- Run the project
  - On `\GradePro-repo`
    - ` python .\manage.py runserver`
- Access the admin panel
  - Go to http://localhost:8000
    - Port may differ if you change it on "runserver" command.
- Access to urls
  - `calculadora/resultado/`