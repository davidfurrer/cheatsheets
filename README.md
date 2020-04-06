# cheatsheets

## Linux

| Command                                   | Description                                                 |
| ----------------------------------------- | ----------------------------------------------------------- |
| `df -h /`                                 | Show total free disk space                                  |
| `ls -haltr`                               | list files by date (human readable, reversed)               |
| `du -sh folder`                           | Show size of folder                                         |
| `ls \| wc -l`                             | Number of files in folder                                   |
| `rm -r mydir`                             | Delete folder                                               |
| `cp -avr home/sourcedir home/destinydir`  | Copy folder with all content                                |
| `echo hello > $(date +%Y%m%dT%H%M%S).txt` | Saves output of command in file <br> with timestamp as name |
| `mkdir -p folder/{1..10}`                 | Make 10 subfolders                                          |
| `ctrl + z`                                | suspend running process                                     |
| `ps f`                                    | show processes                                              |
| `fg`                                      | resume stopped process (in foreground)                      |
| `bg`                                      | resume stopped process (in background)                      |
| `jobs`                                    | show jobs                                                   |
| `kill <PID>`                              | kill process with ID <PID>                                  |
| `sleep 360 &`                             | starts sleep command in background                          |
| `cat /etc/os-release`                     | show which linux distro is installed                        |
| `rwx, 421 (e.g. chmod 600 <file>)`        | change permissions                                          |
| `mv/cp <old> <new>`                       | rename/copy  file                                           |
| `ls/rm *.mp3`                                | list/delete all mp3                                                |
| `cd`                                | same as  `cd ~`                                              |
| `pushd` <folder>, `popd`                                  | go into folder, go back where you came from                                            |
| `file song.mp3`                                | shows type of file, here: mp3                                         |
| `locate <file name>`                                | find <file name>                                           |
| `sudo updatedb `                                | update db for locate                                        |
| `cal`                                | show calender                                           |
| `whatis scp`                                | return: secure copy (remote file copy program)                                         |
| `apropos time`                                | show commands related to time                                          |
| `man time`                                | show manual for time                                          |
| `cat >> file, ctrl-d to exit`                                | opens editor and saves what you write in file                                          |
| `cat file1 file2`                                | concatenates files                                          |
| `more/less file2`                                | pager/scroller for file2                                          |
| export PATH=/home/pi/.local/bin:$PATH  | add to path in .bashrc |
|pkill -u [username] | kill all processes belonging to [username]|
|`ifconfig \| grep inet`|get ip|
  
  

## Github

| Command                                                                          | Description                                                                                                    |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `git rm --cached <filename>`<br> `commit and push`                               | Remove file on origin master                                                                                   |
| `git log --oneline`                                                              | print logs only as one line                                                                                    |
| `git config --global --edit`                                                     | change global default of comitter (name, email)                                                                |
| `git branch <branch-name>`                                                       | create new branch                                                                                              |
| `git checkout <branch-name>`                                                     | switch to <branch-name> (can also be a remote one)                                                             |
| `git checkout -b <branch-name>`                                                  | create new branch <branch-name> and switch to it                                                               |
| `git push origin --delete <branch-name>`                                         | delete remote branch                                                                                           |
| `git branch -d <branch-name>`                                                    | delete local branch                                                                                            |
| `git stash save 'message'`                                                       | stash changes (undoes everything up to last commit -> git status will now say nothing to commit)               |
| `git stash list`                                                                 | list stashes                                                                                                   |
| `git stash apply stash@{0}`                                                      | restore status of stash, keeps stash                                                                           |
| `git stash pop`                                                                  | same as git stash apply stash@{0} but drops stash, takes first entry in list (most recent, which has number 0) |
| `git stash drop stash@{0}`                                                       | deletes stash from list                                                                                        |
| `git stash, git checkout <branch-name>, git stash pop`                           | stashes carry over to other branches                                                                           |
| `git rebase -i HEAD~2`                                                           | rewrite last commit message                                                                                    |
| `git rebase -i HEAD~2, edit, git reset HEAD^, add/commit, git rebase --continue` | split commit message                                                                                           |
| `git tag v1.0`                                                                   | make tag/release                                                                                               |
| `git push origin v1.0`                                                           | push release                                                                                                   |
| `git checkout -b <branch name> v1.0`                                             | checkout release                                                                                               |
| `git merge origin/master`                                                        | merge origin/master                                                                                            |
| `git pull origin`                                                                | same as git fetch origin, git merge origin/master                                                              |
|`git checkout otherbranch myfile.txt` | Copy a file from one branch to another|
|`git remote set-url origin NEW_URL`| change remote url|

## Github: Fixing common mistakes

| Command                                                                                                                                                                 | Description                                                                        |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `git checkout file.py`                                                                                                                                                  | undo changes up to last commit of file.py                                          |
| `git commit --amend -m 'corrected message'`                                                                                                                             | correct wrong commit message of last commit                                        |
| `git add file.py, git commit --amend`                                                                                                                                   | forgot to add file.py to last commit                                               |
| `git checkout <correct branch>, git cherry-pick <commit hash>, git checkout <wrong branch>, git reset (--soft/--mixed (default)/--hard) <commit hash before wrong one>` | commited on wrong branch                                                           |
| `git clean --df`                                                                                                                                                        | undo untracked changes of files and directories (e.g. when accidentally unzipping) |
| `git reflog, git checkout <hash> (detatched head state), git branch <branch-name>`                                                                                      | go back to certain commit and make branch of this state                            |
| `git reset file.py`                                                                                                                                                     | undo git add file.py                                                               |

## VS Code

| Command           | Description                     |
| ----------------- | ------------------------------- |
| `option-shift-F`  | format file (e.g. with Black)   |
| `cmd-X`           | cut a line                      |
| `shift-cmd-K`     | delete a line                   |
| `cmd-L`           | select the line                 |
| `cmd-Enter`       | insert a new line below it      |
| `shift-cmd-Enter` | insert a new line above it      |
| `⌥↑ and ⌥↓`       | move the line up/down           |
| `shift-cmd-7`     | comment line                    |
| `command-P`       | Opens search palette            |
| `command-shift-P` | Opens command palette           |
| `command-shift-O` | Search by method/function/class |
| `option-shift-F`  | Format file (e.g. with Black)   |
| `control-shift-^` | Open terminal                   |
| `command-J`       | Collapse/ bring back terminal   |
| `:32 (in search)` | Jump to line 32                 |

More vs code shortcuts:
https://gist.github.com/bradtraversy/b28a0a361880141af928ada800a671d9

## Python

| Command                      | Description                        |
| ---------------------------- | ---------------------------------- |
| `python -W ignore script.py` | Run python script without warnings |
| `state = "nice" if is_nice else "not nice"` | ternary operator |

## JavaScript

| Command                      | Description                        |
| ---------------------------- | ---------------------------------- |
| `state = isMember ? '$2.00' : '$10.00'` | ternary operator |

## Oh My Zsh

| Command                      | Description                        |
| ---------------------------- | ---------------------------------- |
| `git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions)` | add autosuggestion |
| `plugins=(zsh-autosuggestions)` | add in ~/.zshrc  |


https://github.com/zsh-users/zsh-autosuggestions

## Conda

| Command                      | Description                        |
| ---------------------------- | ---------------------------------- |
| `conda create -n myenv python=3.6` | create conda environment with specific python version |
| `conda env list` | list all environments |
| `conda env remove --name <env-name>` | remove environment |

## google docs

| Command                      | Description                        |
| ---------------------------- | ---------------------------------- |
| `Ctrl + Shift + V` | copy paste withough formatting |
| 1. File -> Spreadsheet settings -> Locale: Switzerland 2. Format -> Number -> Date 3. Sort | sort sheet by European Date |


## poetry (python)

| Command                      | Description                        |
| ---------------------------- | ---------------------------------- |
| `poetry new <project-name>` | start new project, creates the project folder at the same time |
| `poetry add numpy` | add a package |
| `poetry init` | create toml |
| `poetry install` | install dependencies from poetry.lock file |
| `poetry build` | prepare own package for publishing |
| `poetry publish` | publish to PyPI |
| `poetry config http-basic.pypi username password` | setup PyPI credentials |
| `poetry shell` | launches shell | 
| `poetry run python script.py` | run python script within poetry env | 
| `poetry self update` | update |




You should commit the poetry.lock file to your project repo so that all people working on the project are locked to the same versions of dependencies.
 
 ## Chrome

| Command     | Description  |
| ----------- | ------------ |
| `command-R` | Refresh page |
| `option-command left/right-arrow` | switch tabs |

## AWS

| Command                               | Description           |
| ------------------------------------- | --------------------- |
| `scp -i ssh-key-file file name@ip:~/` | Copy file unto remote |
| `aws ecr get-login --no-include-email --region us-west-1` | login into ECR |


## Heroku

| Command                               | Description           |
| ------------------------------------- | --------------------- |
| `heroku login, heroku create, git push heroku master, heroku ps:scale web=1, heroku open` | deploy app |


## screen

| Command        | Description           |
| -------------- | --------------------- |
| `screen`       | start session         |
| `screen -ls`   | show running sessions |
| `screen -r`    | reattach session      |
| `Ctrl + a + d` | detach from session   |

## SoX

| Command        | Description           |
| -------------- | --------------------- |
| `sox in.wav out4.wav silence 1 0.1 1% -1 0.1 1%`       | Trimming all silence        |
| `sox in.wav out5.wav silence 1 0.1 1% -1 0.5 1%`       | Trimming all silence, Ignoring short periods of silence      |
| `sox in.mp3 -b 16 -e signed-integer -r 16000 -t out.wav` | Convert mp3 to wav     |
| `sox in.wav out.wav remix 1` | only keep 1 channel (if several, e.g. stereo)    |


## pipenv

| Command          | Description                               |
| ---------------- | ----------------------------------------- |
| `pipenv install` | uses Pipfile and installs listed packages |
| `pipenv shell --python python3` | create env with specific python version (can be a path as well)|


## docker

| Command                                      | Description                   |
| -------------------------------------------- | ----------------------------- |
| `docker exec -it <container name> /bin/bash` | ssh into running container    |
| `docker rm $(docker ps -a -q)`               | delete all stopped containers |
| `docker system df`                           | show disk usage               |


## vim

| Command | Description     |
| ------- | --------------- |
| `i`     | insert aka edit |
| `:q`    | quit            |
| `:wq`   | save and exit   |

## datetime (python)

| Command | Description     |
| ------- | --------------- |
| `datetime.datetime.strptime(d, "%Y-%m-%d_%H-%M-%S")`     | convert string (d) to datetime object  |
| `dt.strftime("%Y-%m-%d_%H-%M-%S")`    |  convert datetime object (dt) to string         |


## re (python)

| Command | Description     |
| ------- | --------------- |
| `re.sub('[^a-zA-Z]+', '', string)`     | only keep alphabetical characters  |
| `bool(re.search('is', 'is it'))`     | check if string matches pattern  |

## kubeflow

| Command | Description     |
| ------- | --------------- |
| `kubectl get pods`     | list pods  |

## nvidia GPU

| Command | Description     |
| ------- | --------------- |
| `sudo nvidia-smi --gpu-reset -i 0`     | reset gpu if usage high  |
| `sudo fuser -v /dev/nvidia*`     | check which processes might be using the GPU |

1. log out of the username that issued the interrupted work to that gpu

2. as root, find all running processes associated with the username that issued the interrupted work on that gpu:

ps -ef|grep username

3. as root, kill all of those

4. as root, retry the nvidia-smi gpu reset

## sql

| Command                                                                           | Description              |
| --------------------------------------------------------------------------------- | ------------------------ |
| `pd.read_sql_table('table_name', 'sqlite:///db_file.sql')`                        | read sql database table  |
| `engine = create_engine('sqlite://', echo=False), df.to_sql('users', con=engine)` | save df as sql data base |

## Markdown

| Command                                     | Description | Result                                                     |
| ------------------------------------------- | ----------- | ---------------------------------------------------------- |
| `![](https://media.giphy.com/media/WZ4M8M2VbauEo/giphy.gif)` | insert gif  | ![](https://media.giphy.com/media/WZ4M8M2VbauEo/giphy.gif) |


## jupyter

| Command | Description     |
| ------- | --------------- |
| `jupyter notebook --no-browser --port=8881`     | on remote  |
| `ssh -N -f -L localhost:8882:localhost:8881 ubuntu@<instance_IP> -i ~/.ssh/<aws-key-file>.pem`     | locally  |


## tensorboard  

| Command | Description     |
| ------- | --------------- |
| `tensorboard --logdir logs/models/ &> logs/tboard.log & disown`     | launch tensorbard (port 6006)  |
| `tensorboard --logdir artifacts &> logs/tboard.log & disown`     | launch tensorbard (port 6006), different folder  |



## Matplotlib

#### Save fig
```python
plt.plot(x)
plt.savefig('name.png', bbox_inches='tight')
plt.close()
```
### Nice theme
```python
plt.style.use("fivethirtyeight")
```

## Define figure size

```python
fig = plt.figure(figsize=(18,3))
ax = fig.add_subplot(1, 1, 1)
ax.plot(x)
```

### Common Snipptes

```python
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

df = pd.read_csv('')
```

### Reshaping model inputs

#### e.g. batched LSTM
```python
[(None, None, x), (None, None, y)] 
 model.predict([df1.values.reshape(1, -1, x), df2.values.reshape(1, -1, y)])
```

### Loading h5 file
```python
tf.keras.models.load_model(model_path, custom_objects={'keras': tf.keras, 'tf': tf}, compile=False)
```

### multi-processing
```python
from joblib import Parallel, delayed

def process_files(key):
    # do stuff

Parallel(n_jobs=4)(delayed(process_files)(key) for key in tqdm.tqdm(key_list))
```

### copy files s3

```python
import boto3
s3 = boto3.resource('s3')

for file_name in file_list:
    s3.Object(<bucket>, f'{destiny}/{file_name}').copy_from(CopySource=f'<bucket>/{file_name}')
```

### list files s3 bucket

```python
import boto3
s3 = boto3.resource('s3')

my_bucket = s3.Bucket('bucket_name')

for file in my_bucket.objects.all():
    print(file.key)
```

## seaborn

| Command | Description     |
| ------- | --------------- |
| `ax = sns.scatterplot(x="total_bill", y="tip", data=tips)`     | scatter  |

### try/except/else/finally

```python
def foo():
    try:
        1/0
    except Exception as e:
        print(f'caught {e} exception')
    else:
        print('no exception raised')
    finally:
        print('finally')
```

## Docstrings 

### Google style

```python
def function_with_pep484_type_annotations(param1: int, param2: str) -> bool:
    """Example function with PEP 484 type annotations.
    
    More detailed description of function.
    
    Args:
        param1: The first parameter.
        param2: The second parameter.

    Returns:
        The return value. True for success, False otherwise.
        
    Examples:
        Examples should be written in doctest format, and should illustrate how
        to use the function.

        >>> print([i for i in example_generator(4)])
        [0, 1, 2, 3]

    """



def benchmarkFeed(name: str, target: int, size: int, iters: int) -> float:
    """Runs a microbenchmark to measure the cost of feeding a tensor.

    Reports the median cost of feeding a tensor of `size` * `sizeof(float)`
    bytes.

    Args:
        name: A human-readable name for logging the output.
        target: The session target to use for the benchmark.
        size: The number of floating-point numbers to be feed.
        iters: The number of iterations to perform.
      
    Returns:
        Cost of feeding a tensor.
      
    """
```

https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

## Simple class example

```python
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.treats_eaten = 0

    def give_treats(self, count):
        self.treats_eaten += count
```

## Star args example (*args)

Optional positional arguments

```python
def log(message, *values):
    if not values:
        print(message)
    else:
        value_strings = ', '.join(str(x) for x in values)
        print(f'{message}: {value_strings}')
        
log('My numbers are', 1, 2) # My numbers are: 1, 2
log('Hi there') # Hi there
favorites = [2, 3, 4]
log('Favorites', *favorites) # Favorites: 2, 3, 4
log('Favorites', favorites) # Favorites: [2, 3, 4]
```

## None as default value

Default arguments are only evaluated once: during function definition at module load time. 

```python
def log(message, when=None):
    when=datetime.now() if when is None else when
    print(f'{when}: {message})
```

## Open/ write json

```python
with open('data.txt') as json_file:
    data = json.load(json_file)
    
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
```

## webscraping

```python
from bs4 import BeautifulSoup
import requests


page = requests.get(start_link)
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find('table', {'class': 'mega-table'})
names = table.findAll('td', {'class': 'player-cell'})

namelist = list()
for name in names:
    namelist.append(name.get_text())
```


## print line

```python
print_line = "-".center(100, "-")
print(print_line)
```

## list of types in python

```python
from typing import List, Set, Dict, Tuple, Optional
```


| type                    | Description                        |
| ---------------------------- | ---------------------------------- |
| `None` |  |
| `bool` |  |
| `int` |  |
| `float` |  |
| `str` |  |
| `Tuple` |  |
| `List` |  |
| `Dict` |  |
| `pd.DataFrame` |  |

https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

## git rebase

```
git pull origin master
git checkout <branch-id>
git add file.py
git commit -m 'added file.py'
git push 
git checkout master
git pull
git checkout <branch-id>
git rebase -i master
resolve conflicts
git push --force
```

## python linters

flake8, 

## python formatters

black, yapf



