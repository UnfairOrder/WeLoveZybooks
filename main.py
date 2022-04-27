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

def NextChapter(driver):
    driver.find_element(By.CLASS_NAME,'nav-text').click()

def BusyworkBot(driver):
    print("testing line")

#Multiple Choice
    multiple_choice_count = 0
    Mult_Choice = driver.find_elements(By.CLASS_NAME ,"question-choices")
    multiple_choice_count += 1
    print("Located questions")
    print(Mult_Choice)
    for Question in Mult_Choice:
        Options = Question.find_elements(By.XPATH,'./child::*')
        for button in Options:
            button.click()
            time.sleep(0.125)
            Main_Question = Question.find_element(By.XPATH,"..")
            Response = Main_Question.find_element(By.XPATH,"./following-sibling::*")
            if Response.get_attribute("class")=="zb-explanation has-explanation correct":
                print("It's right!")
                break

    time.sleep(2)
    print("participation assignments")

#Participation assignments
    viewing_assignment_controls = driver.find_elements(By.CLASS_NAME, "animation-controls")
    print("Controls found")
    print(viewing_assignment_controls)
    participation_assignment_count = 0
    for assignment in viewing_assignment_controls:
        participation_assignment_count +=1
        buttons = assignment.find_elements(By.XPATH,'./child::*')
        for button in buttons:
            driver.execute_script("arguments[0].click();", button)

    #Loop for play button clicking
    while (True):
        play_buttons = driver.find_elements(By.CLASS_NAME, 'play-button') #This works to detect the play button
        if play_buttons == []:
            print("failed search")
        else:
            print("success!")
            for b in play_buttons:
                print(b)
        for button in play_buttons:
            print(button.get_attribute('class'))
            if button.get_attribute('class') == 'play-button bounce':
                driver.execute_script("arguments[0].click();", button) #This is crucial and works

        completed_boxes = driver.find_elements(By.CLASS_NAME,'zb-chevron')
        i=0
        for item in completed_boxes:
            if item.get_attribute("class") == 'zb-chevron check title-bar-chevron orange  filled  large':
                i+=1
        time.sleep(1)
        if i==participation_assignment_count+multiple_choice_count:
            break
    time.sleep(3)
#TODO make the window a little nicer
    # TODO add something to show the program is still running.


# Driver Initialization
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# Opening Zybooks
driver.get("https://www.zybooks.com/")
driver.maximize_window()  # Fullscreen to minimize Element searches
time.sleep(5)  # Wait for Browser to Load

# Find and Click Sign in
sign_in_button = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/div/div/nav/div/ul/li[7]/a/span[2]')
sign_in_button.click()


#Root Window creation
root = Tk()
root.title("We love Zybooks")
root.geometry("400x250")

#Title Label
Title = Label(root, text="We love Zybooks", font=("Arial",25))
Title.pack(side = "top")

#Subtitle Label
subTitle = Label(root, text="press start once a chapter is selected", font=("Arial", 14))
subTitle.pack(side="top")

#start button
start_button = Button(root, text="Start", fg='blue', command=lambda: [BusyworkBot(driver)], font=("Arial", 25))
start_button.pack(side="bottom")

#next Chapter button
next_chapter = Button(root ,text = "Next Chapter", fg='green',command=lambda:[NextChapter(driver)], font=("Arial",25))
next_chapter.pack(side="bottom")

wait_button = messagebox.showinfo("Please sign in")

root.mainloop()

