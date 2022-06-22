# call system wide script
from ast import For
from alive_progress import alive_bar
from time import sleep
from git import Repo
from sys import argv

MSG = ''.join(argv[1:]) # <- "I like this format"
PATH_OF_GIT_REPO = r'../'  # .git 
COMMIT_MESSAGE = MSG

def dotGitExist() -> str:
    ''' Check for the existance of a .git dir '''
    pass 

def progressor():
    '''Terminal status'''
    with alive_bar(100) as bar:  
        for i in range(100):
            sleep(0.03)
            bar()                       

    # using bubble bar and notes spinner
    with alive_bar(200, bar = 'bubbles', spinner = 'notes2') as bar:
        for i in range(200):
            sleep(0.03)
            bar()                        

def gitupdater() -> str:
    '''automate updating repo dir'''
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.pull('origin')
        repo.git.add(['.'])
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
        progressor()
    except:
        print('Error occured while pushing the code')    

gitupdater()

