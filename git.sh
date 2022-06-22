# to clone repository to a local directory
git clone (url to repository)

# to create new repository 
git init newrepo

# adding remore repository (following "git init") - 
    # create a repositoy on github with the name of the folder and copy the URL from the clone command
git remote add origin https://github.com/eandtsa/testnewrepo.git 

# check remote repository configuration (following "git init")
git remote -v
origin  https://github.com/eandtsa/testnewrepo.git (fetch)
origin  https://github.com/eandtsa/testnewrepo.git (push)

# to remove remote (following "git init")
git remote rm origin
git remote -v


# status of the file ?
git status

# adding removing files
git add .
git add -A 
git add (filename)

# remove file from git
git rm -f (filename)

# rename file in git
git mv -f (source) (destination)

# commit changes 
git commit -a -m "comment"

# push files to remote repository
git push origin main 

# pull remote updates to local repository
git pull origin main

# snapshots of commits, 40 charater SHA string
git log 

# add branch 
git branch testbranch 

git branch
* main
  testbranch

#switch branch
git checkout testbranch
Switched to branch 'testbranch'

git branch
  main
* testbranch

# create and swtich branch
git checkout -b newbranch02
Switched to a new branch 'newbranch02'

git branch
  main
* newbranch02
  testbranch

# merge from a branch to the main
git checkout newbranch
# do changes to the file 
git add .
git commit -am "bbb"
git checkout main
git merge newbranch
git push origin main

# diff between working directory and the index
git diff

# diff between index and last commit
git diff --cached

# diff between most recent commit nd current working directory
git diff HEAD