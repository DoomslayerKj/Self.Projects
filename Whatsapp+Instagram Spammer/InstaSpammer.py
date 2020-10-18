#Made by VaradKJ
#Download ChromeDriver in your C drive root
#Works only on Chrome v84

import os,sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from os import system
import getpass
import tkinter as tk
from tkinter import simpledialog
import concurrent.futures

application_window =tk.Tk()

PATH = "C:\chromedriver.exe"
browser=webdriver.Chrome(PATH)
browser.get('https://www.instagram.com')



#NOW AT HOME PAGE
def finding_target():
    target_name = simpledialog.askstring("USER NAME", "Enter the target recipient username(DONT ADD '@'!) : ",
                                    parent=application_window)
    #target_name= input("Enter the target recipient username(DONT ADD '@'!) : ")

    spam_message = simpledialog.askstring("SPAM_MESSAGE", "Enter Spam Message : ",
                                    parent=application_window)
    #spam_message = input("Enter Spam Message : ")
    #time.sleep(3)

    count_times = int(simpledialog.askstring("SPAM COUNT", "Number Of Spam Messages : ",
                                    parent=application_window))
    browser.get("https://www.instagram.com/{}/".format(target_name))

    time.sleep(2)

    message_button = browser.find_elements_by_class_name('_862NM')
    message_button[0].click()
    time.sleep(2)

    send_message(spam_message,count_times)




def send_message(message,no_of_times):
    #NOW AT DMS
    message_entry_field =browser.find_elements_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
    #SENDING SPAM!
    for i in range(no_of_times):
         message_entry_field[0].click()
         message_entry_field[0].send_keys(message)
         message_entry_field[0].send_keys(Keys.ENTER)











if __name__=="__main__":
    #GETTING LOGIN INFO
    username = input('Enter Username : ')
    password = input('Enter Password : ')


    #ENTERING THE INFO
    username_field = browser.find_element_by_name('username')
    username_field.send_keys(username)
    password_field = browser.find_element_by_name('password')
    password_field.send_keys(password)

    #LOGGIN IN
    log_in_button = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
    log_in_button.click()

    time.sleep(5)

    #GETTING RID OF 'SAVE UR LOGIN INFO??'

    not_now_button =browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
    not_now_button.click()

    time.sleep(2)
    #GETTING RID OF 'TURN ON NOTIFICATIONS'
    not_now_button_1 = browser.find_elements_by_xpath('//button[text()="Not Now"]')
    not_now_button_1[0].click()

    finding_target()


#BUGGY FUCKING LOOP, FOR SOME FUCKING REASON WTFFF ..PLS DEBUG IF U CAN

    # choice = int(input("1 = CONTINUE\n0=Exit : "))
    # if choice == 1:
    #     finding_target()
    # else:
    #     browser.quit()
    #     sys.exit()






