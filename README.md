1. Upload a single file using drag-drop or select on the browser.

2. Uploaded file is copied under media folder under your project.

# Usage

1. Pull the code
2. Execute following
    *  ```virtualenv venv```
    *  ```source venv/bin/activate```
    *  ```pip install -r requirements.txt```
    * ```npm init```
    * ```npm install```
    * ```webpack --hot --inline```
    * ```python manage.py runserver```

3. On browser click on the box to upload a picture a file. The selected file is uploaded under /media folder of the django-application.

4. The file will be saved as 'xxx.txt'. If you want to maintain the name of the original file replace:
```javascript
file.append('name', files[0])
```
with
```javascript
file.append('name', files[0], 'xxx.txt')
```
