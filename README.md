# cheatsheets

## Linux

| Command        | Description          |
| ------------- |-------------|
| `df -h /`       | Show total free disk space |
| `du -sh folder`       | Show size of folder |
| `ls \| wc -l`    | Number of files in folder      |
| `rm -r mydir` | Delete folder      |
| `cp -avr home/sourcedir home/destinydir` | Copy folder with all content |
| `echo hello > $(date +%Y%m%dT%H%M%S).txt`| Saves output of command in file <br> with timestamp as name| 
| `mkdir -p folder/{1..10}`|Make 10 subfolders|


## Github

| Command        | Description           |
| ------------- |-------------|
| `git rm --cached <filename>`<br> `commit and push`| Remove file on origin master  |
| `git log --oneline`| print logs only as one line |
|     |       |


## VS Code

| Command        | Description           |
| ------------- |-------------|
|`command-P`| Opens search palette|
|`command-shift-P`| Opens command palette|
|`command-shift-O`| Search by method/function/class |
| `option-shift-F`     | Format file (e.g. with Black) |
|`control-shift-^`| Open terminal|
|`command-J`| Collapse/ bring back terminal|
|`:32 (in search)`| Jump to line 32 |



## Python

| Command        | Description           |
| ------------- |-------------|
| `python -W ignore script.py`     | Run python script without warnings |

## Chrome

| Command        | Description           |
| ------------- |-------------|
| `command-R`     | Refresh page |

## AWS

| Command        | Description           |
| ------------- |-------------|
| `scp -i ssh-key-file file name@ip:~/`     | Copy file unto remote |


## screen

| Command        | Description           |
| ------------- |-------------|
| `screen`     | start session |
| `screen -ls`     | show running sessions |
| `screen -r`     | reattach session |
| `Ctrl + a + d`     | detach from session |



## pipenv

| Command        | Description           |
| ------------- |-------------|
| `pipenv install`| uses Pipfile and installs listed packages |


## docker

| Command        | Description           |
| ------------- |-------------|
| `docker exec -it <container name> /bin/bash`| ssh into running container |
| `docker rm $(docker ps -a -q)`| delete all stopped containers |



