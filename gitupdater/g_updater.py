from alive_progress import alive_bar
from time import sleep
from os import system
from sys import argv
from git import Repo

# maybe create module for var values
FAIL_EXCEPTION = 'Error occured while pushing the code'
PATH_OF_GIT_REPO = r'../'  # .git 
MSG = ''.join(argv[1:]) # <- "I like this format"
REMOTE_NAME = 'origin'
COMMIT_MESSAGE = MSG
SYSTEM_CMD = "clear"
GIT_PULL = 'origin'
ONE_HUNDRED = 100
GIT_ADD = '.'

def dotGitExist() -> str:
    ''' Check for the existance of a .git dir '''
    # if .git exist call gitupdater
    # else, find root dir to check if .git exist
    pass 

def progressor():
    '''Terminal status'''
    with alive_bar(ONE_HUNDRED) as bar:  
        for i in range(ONE_HUNDRED):
            sleep(0.03)
            bar()                       

    # using bubble bar and notes spinner
    with alive_bar(ONE_HUNDRED + ONE_HUNDRED, bar = 'bubbles', 
                        spinner = 'notes2') as bar:
        for i in range(ONE_HUNDRED + ONE_HUNDRED):
            sleep(0.03)
            bar()                        

def gitupdater() -> str:
    '''automate updating repo dir'''
    try:
        progressor()
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.pull(GIT_PULL)
        repo.git.add([GIT_ADD])
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name=REMOTE_NAME)
        origin.push()
        progressor()
    except:
        print(FAIL_EXCEPTION)

def main():
    system(SYSTEM_CMD)
    # call progressor
    progressor()
    # call does dotgitexist
    gitupdater()

main()

