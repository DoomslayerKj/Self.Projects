
#Download ChromeDriver in your C drive root
#Works only on Chrome v84
#DEVELOPED BY @mr.y2kj
#ITS FAIRLY SIMPLE TO USE
#MAKE SURE YOU HAVE CHROME BROWSER INSTALLED
#AND chromedriver.exe   in THE ROOT OF YOUR C DIRECTORY BY DEFAULT
#MAKE SURE TO HAVE SELENIUM INSTALLED TOO

#DIRECTIONS TO USE
#IT WILL OPEN WHATSAPP WEB ON CHROME
#YOU JUST HAVE TO SCAN THE QR CODE
#AND FILL IN THE DETAILS OF {WHOM TO SPAM,HOW MANY TIMES,WHAT TO SPAM WITH} AND YOU'LL BE GOOD TO GO

from selenium import webdriver
from selenium.webdriver.common.keys import Keys  #to gain access to enter,escape and all
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import os,sys
from os import system


#Gathering Info on Target
def spam_same(name):

    number_of_spam = int(input("Enter The Number of times to be spammed: "))
    message_choice = int((input("1 to send Custom message\n2 to send Random Emojis\n=")))
    if message_choice == 1:
        message_body = (input("The spam message? : "))
    elif message_choice == 2:
        with open('emojis.txt') as emoji_file:
            message_body = emoji_file.read()
    whatsapp_spam_new(name, number_of_spam, message_body)

def gather_info_new(name=None):
    name = input("\nEnter the Name of the Recipient: ")
    number_of_spam=int(input("Enter The Number of times to be spammed: "))
    message_choice = int((input("1 to send Custom message\n2 to send Random Emojis\n=")))
    if message_choice == 1:
        message_body = (input("The spam message? : "))
    elif message_choice == 2:
        with open('emojis.txt',encoding="utf8") as emoji_file:
            message_body=emoji_file.read()
    whatsapp_spam_new(name,number_of_spam,message_body)


def whatsapp_spam_new(name,spam_times,message):

    user = browser.find_element_by_xpath('//span[@title="{}"]'.format(name))
    user.click()
    input_text_box = browser.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    #FINDING USER AND CLICKING INPUT BOX

    # browser.close()
    # print(e)
    # sys.exit()


    for i in range(spam_times):
        input_text_box[0].send_keys(message)
        input_text_box[0].send_keys(Keys.ENTER)

    print("\n1-New Spam\n2:Same Person Spam\nAnything else to exit\n")
    choice = int(input("="))
    if choice == 1:
        gather_info_new()
    elif choice == 2:
        spam_same(name)
    else:
        print("... Quitting")
        browser.quit()
        sys.exit()



if __name__ == '__main__':
    # Getting PreRequisites and Starting Browser
    PATH = ('C:\chromedriver.exe')
    browser = webdriver.Chrome(PATH)
    browser.get('https://web.whatsapp.com')


    break_seq = False
    print("\nEnter anything after scanning QR code ")
    tmp=input()
    gather_info_new()


