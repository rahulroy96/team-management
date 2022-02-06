A simple team management web application developed in django with features like adding a member to team, editing the details of the members or deleting the members. Each member has a first name, last name, email, phone number and a role. There are two roles admin can delete other members and regular who cant delete.

## Setting up the environment
You need to have [python](https://www.python.org/downloads/) 3.8 or higher, and [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed.

1.  Open a new terminal
2.  Clone this repository

    ```
      git clone https://github.com/rahulroy96/team-management.git
      cd team-management
    ```
3.  Install [pip](https://pip.pypa.io/en/stable/installation/)

    ```
      python -m ensurepip --upgrade
    ```
4.  Install virtualenv
    ```
      pip install virtualenv
    ```
5.  Create the virtualenv, all the dependencies will be installed within this virtual environment.
    ```
      virtualenv venv
    ```
6.  Activate the virtual environment
    ```
      source venv/bin/activate
    ```
7.  Now that the virtual environment is activated you can install the dependencies
    ```
      pip install -r requirements.txt
    ```
    
## Running the application
1.  Before running the application, we first need to create the tables required. This can be done using the migrate command from django
    ```
      python manage.py migrate
    ```
2.  Now that the tables are created, we can run the application. 
    ```
      python manage.py runserver
    ```
    Now open your favorite webbrowser and visit http://localhost:8000
    
## Running the test cases
   We can run the test cases using the below command

    python manage.py test members
