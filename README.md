### To update the environment.yml without creating a new file
    conda env export --no-builds > environment.yml

### To generate/update requirements.txt
    pip freeze > requirements.txt

### To install packages from requirements.txt
    pip install requirements.txt