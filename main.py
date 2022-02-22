#Michael Leoni
#WeLoveZybooks
#CSM
#Version 1.0

import time

from tkinter import Button, Label, Tk, messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#TODO installer
#   Password for install
#   Multi platform
#   hide webdriver console

def BusyworkBot():
#Driver Initialization
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service = service)
#Opening Zybooks
    driver.get("https://www.zybooks.com/")
    driver.maximize_window()    #Fullscreen to minimize Element searches
    time.sleep(1)   #Wait for Browser to Load

#Find and Click Sign in
    sign_in_button = driver.find_element(By.XPATH,'/html/body/div[1]/header/div[2]/div/div/nav/div/ul/li[7]/a/span[2]')
    sign_in_button.click()

#Messagebox for sign in prompt
    messagebox.showinfo(title="Sign in", message="Please Sign in, then press OK.")
    time.sleep(0.5)
#Find and Select Mines CSCI 101 book
    CompSci = driver.find_element(By.XPATH,'//*[@id="ember28"]')
    CompSci.click()

#User Chapter select prompt
#FIXME  change to say click okay after selecting chapter
    messagebox.showinfo("Chapter Select", "Select Lesson / Chapter")

#Find voyeur assignments and 2x check boxes
    #TODO change voyeur assignments to search by class name
#    voyeur_assignment_start = driver.find_elements(By.XPATH, '//*[@id="ember466"]/div[1]/div[1]/button/span')
#    voyeur_assignment_2x = driver.find_elements(By.XPATH, '//*[@id="ember467"]')

#Check 2x boxes for all voyeur_assignments
   # for i in voyeur_assignment_2x:
       # i.click()
#Click all start boxes for voyeur_assignments
   # for i in voyeur_assignment_start:
    #    i.click

#Find Multiple Choice Questions

    Mult_Choice = driver.find_elements(By.CLASS_NAME ,"question")
    print("Located questions")
    print(Mult_Choice)
#Interate through list
    for question in Mult_Choice:
       print("Starting loop")
       #FIXME options list empty
       #    bad xpath likely / change to find classname or something
       options = question.find_elements(By.XPATH,'.//input[@type = "radio" and @name = "32"]' )
       print("Options located")
       print(options)
       for bubble in options:
            bubble.click()
            print("Bubble Clicked")
            #Fixme The message object is outside the question class on the webpage
            #   This means I need to reconfigure this to search for all the message objects and line them up 1:1 for the loops
            answer = question.find_element(By.CLASS_NAME,'message').text()
            if answer == "Correct":
                print("Correct answer found")
                break

    time.sleep(12)
    driver.quit()
    #TODO Complete Chapter / Assignment
    #   Multiple Choice Questions
    #       Store Question Elements in list
    #           Search Question for Options
    #           Search Question for answer selection
    #           Break loop if answer is correct



#TODO make the window a little nicer
#Root Window creation
root = Tk()
root.title("We love Zybooks")
root.geometry("400x250")
#Title Label
Title = Label(root, text="We love Zybooks", font=("Arial",25))
Title.pack(side = "top")
#Subtitle Label
subTitle = Label(root, text="I used the Zybooks to destroy the zybooks", font=("Arial", 14))
subTitle.pack(side="top")
#start button
start_button = Button(root ,text = "Start", fg='blue',command=lambda:[root.withdraw(),BusyworkBot()], font=("Arial",25))
start_button.pack(side="bottom")
root.mainloop()