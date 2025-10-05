**macOS Installation:**
1. Download `Estimate-Generator-MacOS.zip`
2. Unzip it  
3. Try **Right-click** `Estimate-Generator.app` → **Open**
4. If blocked, go to **System Preferences → Security & Privacy → General** → Click **"Open Anyway"**
5. Drag to Applications folder

### To update the environment.yml without creating a new file
    conda env export --no-builds > environment.yml

### To generate/update requirements.txt
    pip freeze > requirements.txt

### To install packages from requirements.txt
    pip install requirements.txt