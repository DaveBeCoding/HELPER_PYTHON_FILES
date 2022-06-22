# call system wide script
from git import Repo
from sys import argv

# add a msg to the command line when calling script <-
# add msg to script var to be used <-
msg = ''.join(argv[1:])

# call git add . <-
# once that msg is available add it to git -m "msg" <-
# need bytes for double quotes, pure python <-

# call git push <-

PATH_OF_GIT_REPO = r'../'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'this is a test commit comment'

def git_push():
    # try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    # except:
        # print('Error occured while pushing the code')    

git_push()