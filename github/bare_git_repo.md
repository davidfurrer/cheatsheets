# bare git repo

## description

workspace: certain branch, certain commit

repository: .git


repo: workspace + repository

bare repo: repository

## commands

| Command        | Description          |
| ------------- |-------------|
| `git clone --bare <repo> <bare repo>`       | Clone repo as bare repo (.git folder) |
| `git clone <bare repo>`       | Clone bare repo |
| `git remote -v`       | shows that bare repo is remote|