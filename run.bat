cd %~dp0
set action=%1
if not defined action set action=help
goto %action%

:create_venv
python312 -m venv .venv
.venv\scripts\activate
pip install requirements.txt
goto end

:startproject
call :activate_venv
djang-admin startproject decap .
goto end

:startapp
call :activate_venv
django-admin startapp app
goto end

:create_superuser
call :activate_venv
django-admin createsuperuser
:: jindrich, password related to decap
goto end

:activate_venv
if not exist .venv\Scripts\activate.bat call :create_venv
if not "%VIRTUAL_ENV%" == "" goto end
.venv\scripts\activate
goto end

:dump_data
call :activate_venv
python manage.py dumpdata pages --format=yaml --indent=2 > pages\fixtures\pages.yaml
goto end

:load_data
call :activate_venv
python manage.py loaddata pages\fixtures\pages.yaml
goto end

:help
echo Usage: run.bat ^<action^>
echo Actions:
echo    create_venv     - Create a virtual environment and install dependencies
echo    startproject    - Start a new Django project in the current directory
echo    startapp        - Start a new Django app named 'app' in the current project
echo    help            - Show this help message
echo    activate_venv   - Activate the virtual environment
echo    create_superuser- Create a Django superuser
echo    dump_data       - Dump data from 'pages' app to a fixture file  
echo    load_data       - Load data from fixture file to 'pages' app
goto end

:end

