from git import Repo
import pandas as pd
import schedule
import time

PATH_OF_GIT_REPO = r'/Users/Sam/01-Economics'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

def git_push(PATH_OF_GIT_REPO, COMMIT_MESSAGE):
    df = pd.DataFrame({'a': [1,2],'b': [3,4]})
    df.to_csv('/Users/Sam/01-Economics/CSV Files/Macro_Vars.csv')    
    
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(all=True) # , update=True
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    

schedule.every().minute.do(git_push(PATH_OF_GIT_REPO, COMMIT_MESSAGE))
