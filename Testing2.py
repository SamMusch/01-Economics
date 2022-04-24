import schedule
import time

def job():
    print("I'm working...")
 
schedule.every().minute.do(job)
    
#schedule.every().day.at("10:30").do(job)