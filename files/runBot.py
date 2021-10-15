import datetime
import schedule
import time
import moodle as m
import log


def monday():

    print("Logging in, please wait...")
    c = m.AtBot()
    c.logInMoodle()
    print("Logged in! Program started, minimise this window. DO NOT CLOSE IT!")
    schedule.every().monday.at(log.eleven).do(c.csoAtt)
    schedule.every().monday.at(log.fifteen).do(c.mpiAtt)
    while True:
        schedule.run_pending()
        time.sleep(60)
        c.tabRef()
        time.sleep(5)


def tuesday():
    print("Logging in, please wait...")
    c = m.AtBot()
    c.logInMoodle()
    print("Logged in! Program started, minimise this window and the opened chrome window. DO NOT CLOSE IT!")
    schedule.every().tuesday.at(log.eleven).do(c.csoAtt)
    while True:
        schedule.run_pending()
        time.sleep(60)
        c.tabRef()
        time.sleep(5)


def wednesday():
    print("Logging in, please wait...")
    c = m.AtBot()
    c.logInMoodle()
    print("Logged in! Program started, minimise this window and the opened chrome window. DO NOT CLOSE IT!")
    schedule.every().wednesday.at(log.fourteen).do(c.mpiAtt)
    while True:
        schedule.run_pending()
        time.sleep(60)
        c.tabRef()
        time.sleep(5)


def thursday():
    print("Logging in, please wait...")
    c = m.AtBot()
    c.logInMoodle()
    print("Logged in! Program started, minimise this window and the opened chrome window. DO NOT CLOSE IT!")
    schedule.every().thursday.at(log.nine).do(c.mpiAtt)
    schedule.every().thursday.at(log.fifteen).do(c.itwAtt)
    while True:
        schedule.run_pending()
        time.sleep(60)
        c.tabRef()
        time.sleep(5)


def friday():
    print("Logging in, please wait...")
    c = m.AtBot()
    c.logInMoodle()
    print("Logged in! Program started, minimise this window and the opened chrome window. DO NOT CLOSE IT!")
    schedule.every().friday.at(log.nine).do(c.csoAtt)
    schedule.every().friday.at(log.eleven).do(c.mpiAtt)
    schedule.every().friday.at(log.fifteen).do(c.itwAtt)
    while True:
        schedule.run_pending()
        time.sleep(60)
        c.tabRef()
        time.sleep(5)

e = datetime.datetime.now()
day = (e.strftime("%a"))

if __name__ == '__main__':
    print("Welcome! today is ", day)

    if day == "Mon":
        monday()
    elif day == "Tue":
        tuesday()
    elif day == "Wed":
        wednesday()
    elif day == "Thu":
        thursday()
    elif day == "Fri":
        friday()
    else:
        print("No class today!!!")
        exit()
