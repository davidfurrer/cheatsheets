# bare git repo

## description

workspace: certain branch, certain commit

repository: .git


repo: workspace + repository

bare repo: repository

## commands

| Command        | Description          |
| ------------- |-------------|
| `git clone --bare <repo>`       | Clone repo as bare repo (.git folder) |
| `git clone <bare repo>`       | Clone repo as bare repo (no .git folder) |
| `git remote -v`       | remote is bare repo |