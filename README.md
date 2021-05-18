# Space Operation & Control System

Project to build a management system for Milton Keynes Makerspace.

This project is not currently meant for external use, it is currently experimental and written as such. It is not intended for adaptation at this stage, and to do so will require knowledge of Django, if you do so it is of your own accord. Current versions are not production ready, and will require secret key changes etc.



### Currently Implemented
Basic Profiles for member management
Various front end user links, ie links to external forms.
Asset Register started - managed using admin interface. In future will print

## Started
Back End Tool for label printing, currently experimental using PyLabels. Currently plan to have a form which sends data to a node, connected to the label printer for local printing of labels.





## Planned Features 

### Front End 

Django Project 

Web app 

Membership Management - Databases, emails, payments, allow members to make accounts etc. Member Tools, Forms ie broken tools, Storage Label Generation -[]

Automation Control tools - light controller, heat controller etc.  -[]

Access Control Management - Equipment Status - Add/Remove permissions etc Equipment Nodes - Octoprint Nodes etc.  -[]

Data & Statistics - View current states about the space etc. -[]

### Back end

 Docker/Portainer MQTT PostgreSQL Automation Scripts (NodeRed, straight NodeJS/Python etc) Access Control



## Development Environment

Ensure recent version of Python 3 and Pip. Python Virtual environment accessed at 

```Command Line
SOCS\Django\venv\Scripts\activate.bat 
```

In development mode, SQLite is used, therefore tables must be created.

`py manage.py makemigrations` Check for table changes 

`py manage.py migrate` Create/update the database.

You will also need to create a new superuser to access the Django administrative functions.

`py manage.py createsuperuser`

This will ask you to create credentials, then you will be able to log in to /admin

## Acknowledgements
Currently building ontop of an excellent set of tutorials by Corey Schafer https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g
Some icons are used from Font Awesome Free, https://fontawesome.com/