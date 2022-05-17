# UniversalTestProject
Django api which allows to upload an Excel file and define columns, for which returns a summary in json format

## Run
1. In the project main directory setup a virtual environment
```
python -m venv ./venv
```

2. Activate the virtual environment
```
.\venv\Scripts\activate.bat
```

3. Install requirements
```
pip install .
```

4. Run application
```
cd UnversalTestProject
```
```
python manage.py runserver
```

## Api and documentation
The app is running on the http://localhost:8000/home/. <br>
The api is running on the http://localhost:8000/api/. <br>
To see the documentation go to http://localhost:8000/docs/.