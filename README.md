# neurolab-mongo-python

![image](https://user-images.githubusercontent.com/57321948/196933065-4b16c235-f3b9-4391-9cfe-4affcec87c35.png)

### Step 1 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 2 - Run main.py file

```bash
python main.py
```

### Git version

```bash
git -- version
```

### To download Training dataset in vs code

```bash
wget https://raw.githubusercontent.com/avnyadav/sensor-fault-detection/main/aps_failure_training_set1.csv
```

### Check git repository currectly running

```bash
git remote -v
```

### Remove existing git repositiory connected at origin

```bash
git remote remove origin
```

### The git log command is used to view the history of committed changes within a Git repository.

```bash
git log
```

### Add origin

```bash
git remote add origin
```

### To push the branch or you can say to push the changes in the branch to the Github repo

```bash
git push origin main
```

### See the hidden folder
```bash
ls -a
```

### Go to any folder
```bash
cd <folder name>/
```

### See files of the folder
```bash
ls
```

### Come out of the folder
```bash
cd ..
```

### Change the position of head ---> main
```bash
git reset --soft <commit id >
git reset --soft 6afd
```

### Add new file
```bash
git add.
```

### Check status
```bash
git status
```

## Configure Email id
```bash
git config --global user.email "you@example.com"
```


## Configure user name
```bash
git config --global user.name "Your Name"
```


## Create new commit
```bash
git commit -m "This is our first version code"
```


## Push the commit in the local branch forcefull
```bash
git push origin main -f

After this all file from vs code are uploaded to github repositiory
```


## Add new file .gitignore
``` bash
git add .
git commit -m "Added a new file .gitignore"
```


## removed two blank space 
```bash
git add .
git commit -m "removed two black space from data_dump.py file"
```
