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
| `ctrl + z`|suspend running process|
| `ps f`|show processes|
| `fg`|resume stopped process (in foreground)|
| `bg`|resume stopped process (in background)|
| `jobs`|show jobs|
| `kill <PID>`|kill process with ID <PID>|
| `sleep 360 &`|starts sleep command in background|
| `cat /etc/os-release`|show which linux distro is installed|




## Github

| Command        | Description           |
| ------------- |-------------|
| `git rm --cached <filename>`<br> `commit and push`| Remove file on origin master  |
| `git log --oneline`| print logs only as one line |
| `git config --global --edit`  | change global default of comitter (name, email)      |
| `git branch <branch-name>`| create new branch |
| `git checkout <branch-name>`| switch to <branch-name> (can also be a remote one) |
| `git checkout -b <branch-name>`| create new branch <branch-name> and switch to it |
| `git push origin --delete <branch-name>`| delete remote branch |
| `git branch -d <branch-name>`| delete local branch |
 

## VS Code

| Command        | Description           |
| ------------- |-------------|
| `option-shift-F`     | format file (e.g. with Black) |
| `cmd-X`              | cut a line |
| `shift-cmd-K`        | delete a line |
| `cmd-L`              | select the line |
| `cmd-Enter`          | insert a new line below it |
| `shift-cmd-Enter`    | insert a new line above it |
| `⌥↑ and ⌥↓`          | move the line up/down |
| `shift-cmd-7`        | comment line|
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
| `docker system df`| show disk usage |


## vim

| Command        | Description           |
| ------------- |-------------|
| `i`| insert aka edit |
| `:q`| quit |
| `:wq`| save and exit |


