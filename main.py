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
    messagebox.showinfo(title="Sign in", message="Please Sign in, navigate into a chapter,then press OK.")
    time.sleep(0.5)


#Find voyeur assignments and 2x check boxes
    # viewing_assignment_controls = driver.find_elements(By.CLASS_NAME, "animation-controls")
    # print("Controls found")
    # print(viewing_assignment_controls)
    # for assignment in viewing_assignment_controls:
    #     buttons = assignment.find_elements(By.XPATH,'./child::*')
    #     for button in buttons:
    #         button.click()
    # continue_buttons = driver.find_elements(By.CLASS_NAME,"play-button")
    # time.sleep(8)
    # play_buttons = driver.find_elements(By.CLASS_NAME, "play-button bounce")
    # print("Play buttons found")
    # print (play_buttons)
    # for play_button in play_buttons:
    #     play_button.click()

    #Search for Pause buttons. If there are none left break the loop





#Find Multiple Choice Questions

    Mult_Choice = driver.find_elements(By.CLASS_NAME ,"question-choices")
    print("Located questions")
    print(Mult_Choice)
    for Question in Mult_Choice:
        Options = Question.find_elements(By.XPATH,'./child::*')
        if Options != []:
            print("Options found!")
            for i in Options:
                print(i.text)
                i.click()

    time.sleep(12)
    driver.quit()

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