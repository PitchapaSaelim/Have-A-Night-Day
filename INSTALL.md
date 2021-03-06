# Instructions How to Install and Run Locally
## Prerequisite (required) software
|    Name of software    | Versions |
|:----------------------:|:--------:|
|Python|Using at least version 3.7 or higher|
|Django|Using at least version 3.1 or higher|

* **Python** is a programming language that lets you work more quickly and integrate your systems more effectively.
* **Django** is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.

### How to Check Python Version 
> To check the version installed, open a terminal window and entering the following:
* Linux/MacOS:
    ```
    $ python3 –-version
    ``` 
* Windows: 
    ``` 
    ...\> python ––version
    ```

## How to clone Have-A-Night-Day project
* Access to a command-line/terminal window.
    * Linux:
        ```
        CTRL-ALT-T or CTRL-ALT-F2
        ``` 
    * Windows: 
        ``` 
        WIN+R > type powershell > Enter/OK or Type in search tap "cmd"
        ```
    * MacOS: 
        ```
        Finder > Applications > Utilities > Terminal
        ```
* Change directory to the directory that the user wants to run the application.
    ```
    cmd> cd directory name
    ```
* Use git clone in the command line. (Link to clone the project `https://github.com/PitchapaSaelim/Have-A-Night-Day.git`)
    ```
    cmd> git clone https://github.com/PitchapaSaelim/Have-A-Night-Day.git
    ```
## Instructions for setting up a virtual environment (virtualenv)
> **a virtual environment** is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them.
* Access to a command-line/terminal window.
    * Install a virtual environment.
        * Linux/MacOS:
            ```
            $ python3 -m pip install virtualenv
            ```
        * Windows:
            ```
            ...\> python -m pip install virtualenv
            ```    
    * Create new virtual environment.
        * Linux/MacOS:
            ```
            $ virtualenv venv
            ```
        * Windows:
            ```
            ...\> virtualenv env
            ``` 
    * Activate a virtual environment.
        * Linux/MacOS:
            ```
            $ source venv/bin/activate
            ```
        * Windows:
            ```
            ...\> env\Scripts\activate
            ``` 
* *See more details about [Running Python Apps in a Virtual Environment](https://cpske.github.io/ISP/django/virtualenv).*
## Steps needed to configure the application for running
* Access to a command-line/terminal window.
* Change directory to the directory that contain `Have-A-Night-Day` folder.
    ```
    cmd> cd Have-A-Night-Day
    ```
* Install the require packages for this project.
    ```
    cmd> pip install -r requirements.txt
    ``` 
    > Description of the require packages
    * **coverage** is a measure used to describe the degree to which the source code of a program is executed when a particular test suite runs.
    * **django-environ** allows you to use Twelve-factor methodology to configure your Django application with environment variables.
    * **django-crispy-forms** is an application that helps to manage Django forms. It allows adjusting forms’ properties (such as method, send button or CSS classes) on the backend without having to re-write them in the template.
    * **django-extensions** is a collection of custom extensions for the Django Framework.
* Running migrations
    * Linux/MacOS:
        ```
        $ python3 manage.py migrate
        ```
    * Windows:
        ```
        ...\> py manage.py migrate
        ``` 
* Adding initial data to the database.
    * Linux/MacOS:
        ```
        $ python3 manage.py loaddata users.json
        ```
    * Windows:
        ```
        ...\> py manage.py loaddata users.json
        ``` 
## How to start the application and verify it is working
1. **Clone** Have-A-Night-Day project to your machine. [*See how to clone the project.*](https://github.com/PitchapaSaelim/Have-A-Night-Day/blob/master/INSTALL.md#how-to-clone-have-a-night-day-project)
2. Follows the [**setting up a virtual environment**](https://github.com/PitchapaSaelim/Have-A-Night-Day/blob/master/INSTALL.md#instructions-for-setting-up-a-virtual-environment-virtualenv).
3. Follows the [**steps needed to configure the application for running**](https://github.com/PitchapaSaelim/Have-A-Night-Day/blob/master/INSTALL.md#steps-needed-to-configure-the-application-for-running).
4. Access to a command-line/terminal window.
    * Change directory to the directory that contain `Have-A-Night-Day` folder.
        ```
        cmd> cd Have-A-Night-Day
        ```
    * Run the application.
        * Linux/MacOS:
            ```
            $ python3 manage.py runserver
            ```
        * Windows:
            ```
            ...\> py manage.py runserver
            ``` 
            * Terminal window will show like this:
                ``` 
                Watching for file changes with StatReloader
                Performing system checks...

                System check identified no issues (0 silenced).
                November 20, 2020 - 23:20:15
                Django version 3.1, using settings 'Have_A_Night_Day.settings'
                Starting development server at http://127.0.0.1:8000/
                Quit the server with CTRL-BREAK.
                ``` 
    * Follows the link http://127.0.0.1:8000/ in terminal window.
5. **Log in** in the application with this account. 
    ```
    Username: user1
    Password: passworduser1
    ``` 
6. Deactivate virtualenv when you want to quit the server.
    ```
    cmd> deactivate 
    ``` 
