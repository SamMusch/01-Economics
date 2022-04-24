from git import Repo
import pandas as pd


PATH_OF_GIT_REPO = r'/Users/Sam/01-Economics'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

df = pd.DataFrame({
    'a': [1,2],
    'b': [3,4]
})

df.to_csv('/Users/Sam/01-Economics/CSV Files/testing.csv')

def git_push(PATH_OF_GIT_REPO, COMMIT_MESSAGE):
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(all=True) # , update=True
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    

git_push(PATH_OF_GIT_REPO, COMMIT_MESSAGE)

