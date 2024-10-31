# .git projects

## Commit
### To save changes in the local repository
````
git commit -m "Your commit message"
````
## Commit --amend
### To modify the most recent commit
````
git commit --amend -m "Updated commit message"
````
## Merge
### To combine changes from one branch into another
```` 
git merge feature-branch
````
## Rebase
### To reapply commit on top of another base branch
````
git rebase main
````
## Checkout
### To switch to another branch or specific commit
````
git checkout second-branch
````
## Cherry-pick
### To apply a specific commit from one branch onto another
````
git cherry-pick <commit-hash>
````
## Rebase -i
### To interactive edit, reorder, or squash commits in a branch
````
git rebase -i main HEAD~3
````
## Reset 
``for local``
### To create a new commit that undoes changes from a previous commit
````
git revert <commit-hash>
````
## revert
``for local and remote ``
### To create a new commit that undoes changes from a previous commit
````
git revert <commit-hash>
````
## Clone
### To clone someone’s repository
````
git clone https://github.com/ritik48/Wordle-Game.git
````
[gitHub-repository](https://github.com/ritik48/Wordle-Game)
## Push
``Oposit notion for <source:destination> from fetch``
### To upload local changes to the remote repository
````
git push origin main
# also
git fetch origin second-branch:main | git fetch origin <source:destination>
````
## Fetch
``Oposit notion for <source:destination> from push``
### To download updates from a remote repository 
````
git fetch origin main
# also
git fetch origin main:second-branch | git fetch origin <source:destination> 
````
## Pull
### To fetch and merge changes from the remote repository
```
git pull origin main
# also
git pull origin bar:bugFix  # igual to
git fetch origin bar:bugFix; git merge bugFix
```
## Pull --rebase
### To fetch and reapply, commits from the remote branch on top of the local branch
````
git pull --rebase origin main
````
