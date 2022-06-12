
from git import Repo
import pandas as pd

#import nasdaqdatalink
from fredapi import Fred


fred = Fred(api_key='07bccc6cd5cd1018027266ce854705db')

PATH_OF_GIT_REPO = r'/Users/Sam/01-Economics'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

def git_push(PATH_OF_GIT_REPO, COMMIT_MESSAGE):
    df = pd.DataFrame()
    link = ['CPIAUCSL', 'UNRATE', 'DSPIC96']
    for i in link:
        data = pd.DataFrame(fred.get_series(i)).reset_index().tail(60)
        data['Name'] = i
        df = df.append(data)
        
    data = df.pivot(index = 'index', columns = 'Name', values = 0).reset_index().fillna(0)
    data['Updated'] = pd.Timestamp.now()

    data.to_csv('/Users/Sam/01-Economics/CSV Files/Macro_Vars.csv')    
    print(df)
    
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(all=True) # , update=True
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    

git_push(PATH_OF_GIT_REPO, COMMIT_MESSAGE)





#    cpi = nasdaqdatalink.get("FRED/CPIAUCSL").reset_index().tail(40).rename(columns={'Value':'CPI'})
#    unemployment = nasdaqdatalink.get("FRED/UNRATE").reset_index().tail(40).rename(columns={'Value':'Unemployment'})
#    real_disposable = nasdaqdatalink.get("FRED/DSPIC96").reset_index().tail(40).rename(columns={'Value':'Real_Dispose'})
#    df = cpi.merge(unemployment, how='outer', on='Date').merge(real_disposable, how='outer', on='Date')

