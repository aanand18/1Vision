# 1Vision

A Web Application for users to share information and discuss on a particular topic in a room. 
* Users have to login to create a room or join one.
* User can create a profile, if not already having an account, and this profile information in stored in sqlite3 database.
* Users can search for existing rooms and start discussing or can create a room of their own. 
* Users can browse all the rooms based on a certain topic in the "Browse Topics" section.
* Users can see the most recent activities on the site like who messaged in which room and what was the message in the "Recent Activities" section.
* Users can view their or other's profile.



https://user-images.githubusercontent.com/50799286/176783872-55265abc-e773-49fc-a1b0-3fb4ac83b34a.mp4


### Running the project

--> Clone the repository using the command below :
```bash
git clone https://github.com/aanand18/1Vision.git

```

--> Create a virtual environment :
```bash
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv envname

```

--> Activate the virtual environment :
```bash
envname\scripts\activate

```

--> Install the requirements :
```bash
pip install -r requirements.txt

```

#

### Running the App

--> To run the App, we use :
```bash
python manage.py runserver

```

> ⚠ Then, the development server will be started at http://127.0.0.1:8000/

#
