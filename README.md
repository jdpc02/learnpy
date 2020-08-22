# Python Repo for Learning

List the python related locations:
```
python -c "import sys; print(sys.path)"
```


Create a virtual environment for each project:
```
pip install virtualenv
cd <proj_location>
python -m venv <proj_name+env>
```

Running a flask app:
```
set FLASK_APP=somescript.py
python -m flask run
```


Upgrade python modules
```
pip freeze > requirements.txt
Replace == with >= in the requirements.txt file
pip install -r requirements.txt --upgrade
```
