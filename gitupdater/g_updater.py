from os import system, path, chdir, walk
from alive_progress import alive_bar
from sys import argv, exit
from time import sleep
from git import Repo
from vars import *

# FAIL_EXCEPTION = 'Error occured while pushing the code'
# PATH_OF_GIT_REPO = r'../'  # .git
# MSG = ''.join(argv[1:])  # <- "I like this format"
# REMOTE_NAME = 'origin'
# COMMIT_MESSAGE = MSG
# SYSTEM_CMD = "clear"
# GIT_PULL = 'origin'
# ONE_HUNDRED = 100
# GIT_ADD = '.'
# CWD = './.git'
# UP_DIR = '../.git'
# UP_X_TWO = '../../.git'
# CHANGE_UP = '../'
# WALK_NEXT = '.'
# MAX_COUNT = 3
# COUNT_ONE = 1
# SLEEPY_TIME = 0.03

# logic is a bit off ... 
# <gitupdater> needs to know where this
# new location is before being called 
# Bypass <dotGitExist> -> active (uncalled)
def dotGitExist() -> bool:
    ''' Check for the existance of a .git dir '''
    # if .git exist call gitupdater
    count = ONE_HUNDRED - ONE_HUNDRED
    if count > MAX_COUNT:
        print("not found")
        return MAX_COUNT - MAX_COUNT
    if path.isdir(CWD):
        print(".git->cwd")
        # call gitupdater
        # gitupdater()
    else:
        if path.isdir(UP_DIR):
            new_location = chdir(CHANGE_UP)
            print('.git -> up one dir' + str(new_location))
            # call gitupdater
            # gitupdater()
        elif path.isdir(UP_X_TWO):
            print('.git -> up two dir')
            # call gitupdater
            # gitupdater()
        else:
            dir = next(walk(WALK_NEXT))[COUNT_ONE]
            dir_str = ''.join(dir)
            chdir('./'+dir_str)
            count += COUNT_ONE
            dotGitExist()

    # else, find root dir to check if .git exist


def progressor():
    '''Terminal status'''
    with alive_bar(ONE_HUNDRED) as bar:
        for i in range(ONE_HUNDRED):
            sleep(SLEEPY_TIME)
            bar()

    # using bubble bar and notes spinner
    with alive_bar(ONE_HUNDRED + ONE_HUNDRED, bar='bubbles',
                   spinner='notes2') as bar:
        for i in range(ONE_HUNDRED + ONE_HUNDRED):
            sleep(SLEEPY_TIME)
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
    '''Main, call functions to perform github automation .:. Example [g_updater.py "write git message"...]'''
    if len(MSG) < COUNT_ONE:
        input('example input -> g_updater.py "your message to github"')
        exit()
    system(SYSTEM_CMD)
    # call progressor
    progressor()
    # call does dotgitexist
    # dotGitExist()
    gitupdater()


main()
