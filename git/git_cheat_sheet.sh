# Steps
	git status
	# On branch master
	# Your branch is up to date with 'origin/master'.
	# Changes not staged for commit:
	# Untracked files:
	git diff
	# diff --git a/break_time/break_time.py b/break_time/break_time.py
	git add break_time/break_time.py
	git commit -m 'Use cleaner user defined function'
	# [master cd7780e] Use cleaner user defined function
	#  1 file changed, 8 insertions(+), 5 deletions(-)
	git status
	# On branch master
	# Your branch is ahead of 'origin/master' by 1 commit.
	# Untracked files:
	git push origin master
	# Counting objects: 4, done.
	# To https://github.com/asaeles/Udacity-1MAC-Full_Stack.git
	#    c29653c..cd7780e  master -> master

#Git Revision: cheat sheet
# In any command you can reference commits by their SHA, by tags, branches or the special HEAD pointer
# The main difference between the ^ and the ~ is when a commit is created from a merge.
# A merge commit has two parents. With a merge commit, the ^ reference is used to indicate the first parent of the commit
# while ^2 indicates the second parent.
# The first parent is the branch you were on when you ran git merge while the second parent is the branch that was merged in.

#Config Git: First time only
	git config --global user.name “Your full name”
	git config --global user.email “Your email”
	git config --global color.ui auto

#Setup new repository:
	git init # Remember: that command initialize the current directory to a repo.
	git clone URL # Retrieve an entire repository from a hosted location via URL

#Review repository history:
	git status # Displays paths that have differences between the index file and the current HEAD commit
	git show <SHA first characters> # Show specific commit info: commit SHA / author / date / message / patch, SHA is a unique code for every commit
	git show HEAD^^^^^2^ # Shows the parent of the second path in a merge commit done 4 commits behind (so complicated)
	git log # Shows the commit logs
	git log --oneline # Show commit logs in one line
	git log --author="Ahmad" # Author: person how is do the commit
	git log --grep="bug fix"
	git log --stat # To display the file that have changed in the commit, and number of line added or removed. stat == statistics
	git log --patch # Display the actual changed made to a file
	git log --patch --stat # Do the same flag --patch but state show first
	git log --patch -w # Display patch but ignore white space changes
	git log --decorate # Displays branch info and tags, this flag was merged in command git log automatically since GIT v 2.13
	git log --oneline --graph --decorate --all # Show all branches and therefore all commits in the repo
	git shortlog # Group commits by author
	git shortlog -s -n # Show total number of commits per author and sort then numerically

#Commit: Staging and committing
	git diff # Display difference in the files modified in the working area
	git add . # Add all changed files from working to staging (staging all files)
	git add fileName # Staging specific file
	git add fileName1 fileName2 fileName3 # Staging several files
	git commit # Create a commit, open coder, to write commit message
	git commit -a -m 'Commit message' # Stage all changes, create a commit and add message
	git rm --cached fileName # Remove specific file from staging area if it matches work or repo

#Tagging: Labeling a specific commit
	git tag # Display all tags
	git tag -a tagName # Craete a new annotated tag at most recent commit in current branch
	git tag -a tagName SHAcommit # Craete a new tag at specific commit by SHA
	git tag -d tagName # Delete tag
	git tag --delete tagName # Delete tag

#Branching: Allows multiple lines of development
	git branch # List all branches
	git branch branchName # Create a new branch
	git checkout branchName # Switch between branches
	git checkout -b branchName # Create a new branch, and switch to it.
	git branch branchName CommitSHA # Create a branch pointer to a specific commit
	git branch -d branchName # Delete a branch (you cannot delete current branch or a branch with unique commits)

#Merging:
	git merge branchName # Merging branch into current one, you cannot merge current branch

#Undoing changes:
	git commit --amend # Alter the most recent commit (to add staged files and/or edit commmit message)
	git revert commitSHA # Undo the changes, that were made by the provided commitSHA (it makes a new commit to save the new changes)
	git reset HEAD # Does nothing
	git reset HEAD~1 # Undo last commit, move changes to working directory (same as --mixed)
	git reset --mixed HEAD^ # Undo last commit, move changes to working directory
	git reset --soft HEAD~1 # Undo last commit, move changes to staging index
	git reset --hard HEAD^ # Undo last commit, move changes to trash
	git reset # Erase commits, unstaging commits

#Working with remote Repos:
	git remote # Lists remote repos
	git remote -v # Lists remote repos and their fetch and push URLs
	git remote add remoteName remoteURL # Add new remote repe and give it a name
	git remote rename name1 name2 # Rename a remote repo name1 to be name2
	git push origin branch # Send change to remote repo
	git pull origin branch # Retrieve changes from remote repo
	# (doesn't work if local branch has commits not in origin branch, use fetch instead)
	git fetch origin branch # Retrieve changes from a remote repo without
	# syncing the local branch with the origin branch (i.e. create a new branch for origin/master)
	git merge origin/branch # Update local branch to the origin branch
	git rebase -i HEAD~3 # Combine last three commits in that branch interactively
	# Then you'll have to use two 'squash' command and one 'pick' in the editor
	# Preferably use 'reword' instead of 'pick' to edit the message also
	git push -f origin branch # Finally force push the changes to origin
