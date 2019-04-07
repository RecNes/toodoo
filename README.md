# TooDoo App
Django based Simple to do app.

### Technologies Behind:

- Python 3
- Virtual Environment
- Pip
- Django
- Postgresql
- REST Framework
- Jquery
- Bootstrap
- HTML

## Installation on debian based OSes

Please edit secrets-template.txt file to add secrets and rename it to "secrets.txt" for settings.py can read data from this file.

Don't forget to change file permission to 400 for security reason. 

Prepare RDBMS using postgresql
- `# sudo -s` # gain super user priviliges
- `$ su postgres`  # replace to postgresql user
- `$ createuser -DEPRS toodoodbuser`
- `$ createdb -O toodoodbuser toodoo`
- `$ exit`
- `# exit` # return to standard linux user

Clone Project and prepare environment
- `# git clone https://github.com/RecNes/toodoo.git`
- `# cd toodoo`
- `# mkdir logs static_files`
- `# virtualenv -p python3 env`
- `# source env/bin/activate`
- `# pip install -r requirements.txt`

Initiate first migration
- `# python manage.py makemigrations`
- `# python manage.py migrate`

Create super user for admin facilities, optional
- `# python manage.py createsuperuser`

Run project within django development server
- `# python manage.py runserver`

Done! It's ready to use on http://localhost:8000/


### Screen Shot:

![screen shot](https://github.com/RecNes/toodoo/blob/master/media/screenshot.png)

###### Author: Sencer Hamarat
###### Created At: 06/04/2019