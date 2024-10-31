"""
mkdir Story # to create a new directory

cd # Story Change directory

ls # List the directories # An empty directory

touch chapter1.txt # Create an empty file or... called chapter1.txt

pycharm64 chapter1.txt # opens in app the text file # code chapter1.txt for Visual Code

git init # Initialize a new Git repository in the current directory

ls -a # List all files and directories in the current directory, including hidden files and directories

git add chapter1.txt # Stage the file chapter1.txt for the next commit

# # Set a name: git config --global user.name "Your Name"
## Set a email: git config --global user.email "you@exemple.com"

git commit -m "complete chapter 1" # Create a commit with the staged changes and include the message 'complete chapter 1' to describe the changes

git status # Show the current state of the working directory and the staging area

git add . # Stage all changes in the current directory and its subdirectories for the next commit, including new, modified, and deleted files

git diff chapter3.txt # Show the differences between the working directory version of chapter3.txt and the last committed version

git checkout chapter3.txt # Restore chapter3.txt to its last committed state, discarding any changes made to the file in the working directory


git remote add https://github/PROFILE/REPOSITORY.git

git branch -M main

git push -u origin main

"""