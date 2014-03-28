urbanexplorer
=============

urbanexplorer_app is the directory containing the app.
urbanexplorer_server is the directory containing the server.

Installation instructions
-------------------------
The app requires a local installation of PhoneGap (http://phonegap.com/install/)
Once this has been done, the app can be installed by executing

    phonegap install android 

From anywhere in the urbanexplorer_app directory.

I recommend installing from the Google Play Store for convenience, however. https://play.google.com/store/apps/details?id=com.phonegap.urbanexplorer


The server requires Python 2.7.6, pip (https://pypi.python.org/pypi/pip) and a virtualenv is recommended (http://www.virtualenv.org/en/latest/)

Navigate to the root directory where the urbanexplorer_app and urbanexplorer_server directories can be seen. Setup the virtual environment if you are using one, then install the requirements through pip

      pip install -r requirements.txt

Once this has completed, navigate to urbanexplorer_app. Then run

     python manage.py syncdb
     python manage.py migrate
     python manage.py loaddata fixture.json
     python manage.py runserver

and then navigate to the following urls to get data:

127.0.0.1:8000/admin/ (if you set up an admin account)

127.0.0.1:8000/api/v1/?format=json (to see all available REST end points) 


The REST endpoints can be browsed in any browser. The data from the production server is loaded into the database for your perusal.

Please notify me of any issues at 1002253w@student.gla.ac.uk and I will gladly help.