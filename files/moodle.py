##
##	IMPORTANT: CHANGE USERNAME AND PASSWORD INSIDE "Enter Username Here", "Enter Password Here" in logInMoodle(self) METHOD, 
##		   KEEP THE QUOTES!! DO NOT CHANGE ANYTHING ELSE!!
##

#Currently only works on Firefox, as headless chrome is janky. 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.firefox.options import Options
import datetime

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

def AtMarked():
    print("-----------------------------------------------Attendance Marked!-------------------------------------------------")
class AtBot:

    def logInMoodle(self):
        driver.get("https://moodle.iiitn.ac.in/login/index.php")
        elem = driver.find_element_by_name("username")
        elem.clear()
        userN = "Enter Username Here" 
        elem.send_keys(userN)
        elem = driver.find_element_by_name("password")
        passW = "Enter Password Here" 
        elem.send_keys(passW)
        elem.send_keys(Keys.RETURN)
        sleep(2)

    def itwAtt(self):
        print("\n-----------------------------------------------Marking IT Workshop: 1 Attendance------------------------------\n")
        sleep(2)
        driver.get("https://moodle.iiitn.ac.in/course/view.php?id=35")
        elem = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div/section/div/div/ul/li[1]/div[3]/ul/li[3]/div/div/div[2]/div[1]/a/span")
        elem.click()
        sleep(2)
        elem = driver.find_element_by_link_text("Submit attendance")
        elem.click()
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/section/div/div/div[1]/form/fieldset/div/div/div[2]/label[1]/input")
        elem.click()
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/section/div/div/div[1]/form/div[2]/div[2]/div[1]/span/input")
        elem.click()
        driver.get("https://moodle.iiitn.ac.in/login/index.php")
        driver.get("https://moodle.iiitn.ac.in/")
        AtMarked()

    def mpiAtt(self):
        print("\n-----------------------------------------------Marking Microprocessor and Interfacing Attendance---------------------------------\n")
        sleep(2)
        driver.get("https://moodle.iiitn.ac.in/course/view.php?id=102")
        elem = driver.find_element_by_link_text("Attendance")
        elem.click()
        elem = driver.find_element_by_link_text("Submit attendance")
        elem.click()
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/section/div/div/div[1]/form/fieldset/div/div/div[2]/label[1]/input")
        elem.click()
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/section/div/div/div[1]/form/div[2]/div[2]/div[1]/span/input")
        elem.click()
        driver.get("https://moodle.iiitn.ac.in/login/index.php")
        driver.get("https://moodle.iiitn.ac.in/")
        AtMarked()


    def csoAtt(self):
        print("\n-----------------------------------------------Marking Computer System and Organization Attendance---------------------------------\n")
        sleep(2)
        driver.get("https://moodle.iiitn.ac.in/course/view.php?id=106")
        e = datetime.datetime.now()
        day = (e.strftime("%a"))
        if (day == "Mon") or (day == "Tue"):
            elem = driver.find_element_by_link_text("ATTENDANCE FOR MONDAY AND TUESDAY LECTURE")
        else:
            elem = driver.find_element_by_link_text("ATTENDANCE FOR FRIDAY LECTURE")
        elem.click()
        elem = driver.find_element_by_link_text("Submit attendance")
        elem.click()
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/section/div/div/div[1]/form/fieldset/div/div/div[2]/label[1]/input")
        elem.click()
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/section/div/div/div[1]/form/div[2]/div[2]/div[1]/span/input")
        elem.click()
        driver.get("https://moodle.iiitn.ac.in/login/index.php")
        driver.get("https://moodle.iiitn.ac.in/")
        AtMarked()

    def tabRef(self):
        driver.refresh()