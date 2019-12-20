# cheatsheets

## Linux

| Command                                   | Description                                                 |
| ----------------------------------------- | ----------------------------------------------------------- |
| `df -h /`                                 | Show total free disk space                                  |
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



## Python

| Command                      | Description                        |
| ---------------------------- | ---------------------------------- |
| `python -W ignore script.py` | Run python script without warnings |

## Chrome

| Command     | Description  |
| ----------- | ------------ |
| `command-R` | Refresh page |

## AWS

| Command                               | Description           |
| ------------------------------------- | --------------------- |
| `scp -i ssh-key-file file name@ip:~/` | Copy file unto remote |

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


## sql

| Command                                                                           | Description              |
| --------------------------------------------------------------------------------- | ------------------------ |
| `pd.read_sql_table('table_name', 'sqlite:///db_file.sql')`                        | read sql database table  |
| `engine = create_engine('sqlite://', echo=False), df.to_sql('users', con=engine)` | save df as sql data base |

## Markdown

| Command                                     | Description | Result                                                     |
| ------------------------------------------- | ----------- | ---------------------------------------------------------- |
| `![](https://media.giphy.com/media/WZ4M8M2VbauEo/giphy.gif)` | insert gif  | ![](https://media.giphy.com/media/WZ4M8M2VbauEo/giphy.gif) |

## Matplotlib

#### Save fig
```python
plt.plot(x)
plt.savefig('name.png', bbox_inches='tight')
plt.close()
```
### Nice theme
```
plt.style.use("fivethirtyeight")
```

### Common Snipptes

```python
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

df = pd.read_csv('')
```
