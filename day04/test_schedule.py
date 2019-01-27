import schedule,time

def job():
    print("hhhhh")

schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()