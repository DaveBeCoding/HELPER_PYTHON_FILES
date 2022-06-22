# call system wide script
from git import Repo
from sys import argv

# add a msg to the command line when calling script <-
# add msg to script var to be used <-
# msg = ''.join(argv[1:])

# call git add . <-
# once that msg is available add it to git -m "msg" <-
# need bytes for double quotes, pure python <-

# call git push <-

MSG = ''.join(argv[1:]) # <- "my commit msg format"
PATH_OF_GIT_REPO = r'../'  # .git
COMMIT_MESSAGE = MSG

def gitupdater():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.pull('origin')
        repo.git.add(['.'])
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Error occured while pushing the code')    

gitupdater()