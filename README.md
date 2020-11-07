## TDD Excel file download API with Flask and Pandas

### Setup
* Create a virtualenv
```
virtualenv venv

. venv/bin/activate
```
* Install Flask
```
pip install Flask openpyxl
```
or
```
pip install -r requirements.txt
```
* Create a Flask app

### Run Tests
```
python -m unittest tests.test_excel_file_download 
```

### Run Application
```
python app.py
```

### Download File
```
http://localhost:5000/excel/download
```