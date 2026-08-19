import schedule
import time


def job():
    print('oi')

schedule.every(1).second.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)