from faulthandler import disable
from tkinter import Tk, Text, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Label, Style
from turtle import width
import tkinter.font as font
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from numpy import pad
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from urllib.parse import quote
import os
from tkinter.messagebox import askyesno
from tkinter import messagebox


# configration of Tkinter window
root=Tk()
root.iconbitmap('window.ico')
root.geometry('750x550')
root.title('Whatsapp')
f = font.Font(family='System', size=14, weight="bold")
fNum = font.Font(family='System', size=10)


# Set Driver Configration
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")

# Please Change User as per your user
options.add_argument("C:/Users/yk992/AppData/Local/Google/Chrome/User Data/")

os.system("")
os.environ["WDM_LOG_LEVEL"] = "0" 

# For changing color of print statements
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print(style.RED)
print("**********************************************************")
print("**********************************************************")
print("*****                                               ******")
print("*****  THANK YOU FOR USING WHATSAPP BULK MESSENGER  ******")
print("*****      This tool was built by Yogesh Kumar      ******")
print("*****                    8384855717                 ******")
print("*****                                               ******")
print("**********************************************************")
print("**********************************************************")
print(style.RESET)


# Upload excel file
def upload_file():
    f_types = [("xlxs files", ".*xlsx")]   # type of files to select 
    filename = tk.filedialog.askopenfilename(multiple=False,filetypes=f_types)
    f = r"{}".format(filename)
    df = pd.read_excel(filename)
    numbers=df.Number

    txt=''
    counter=1
    for i in numbers:
        txt=txt+'+'+str(i)+'\n'
        counter=counter+1
    
    numbersList.config(text=txt)
    with open("numbers.txt","w") as nFile:
        nFile.write(txt)
    

'''
Send Whatsapp Messages in Bulk 
'''
def start():
    messageText=area.get(1.0, "end-1c")
    with open("message.txt","w") as nFile:
        nFile.write(messageText)
    area.config(state='disabled')
    fileUpload.config(state='disabled')
    startbtn.config(state='disabled')

    messagebox.showinfo("Whatapp QR Scan", "Please logging into Whatsapp Web") # Information Box

    send()
    fileUpload.grid_remove()
    startbtn.grid_remove()
    l1.grid_remove()
    l2.grid_remove()
    area.grid_remove()
    numbersHeading.grid_remove()
    numbersList.grid_remove()

    thanksMessage.config(text="Thanks for using Matra's Application \n See you again") # show thanks message after completion



l1 = Label(root, text = "Upload Excel File",font=f) #File Upload Text
l1.grid(row = 0, column = 0, sticky = W, pady = 10,padx=15)

fileUpload = Button(root, text="Upload File",command=upload_file) #file Upload Button
fileUpload.grid(row=1, column=0)


l2 = Label(root, text = "Message",font=f) #message box lable
l2.grid(row = 2, column = 0, sticky = W,padx=15)

area = Text(root,width='40',height='20') #textbox
area.grid(row=3, column=0,
padx=15,pady=10, sticky=E+W+S+N)

#start Button to start process when the process is started all the fileds are disable
startbtn = Button(root, text="Start",command=start) 
startbtn.grid(row=4, column=0)


numbersHeading = Label(root, text="Numbers",font=f) #number heading 
numbersHeading.grid(row=0,column=4,padx=20)


numbersList = Label(root, text="") #showing number list after file upload
numbersList.grid(row=2,column=4,padx=30)


thanksMessage = Label(root, text="",font=f) #thanks message show after the process completions
thanksMessage.grid(row=3,column=3,padx=30)





# this is function use to send message using selenium and driver
def send():
    f = open("message.txt", "r")
    message = f.read()
    f.close()

    print(style.YELLOW + '\nThis is your message-')
    print(style.GREEN + message)
    print("\n" + style.RESET)
    message = quote(message)

    numbers = []
    f = open("numbers.txt", "r")
    for line in f.read().splitlines():
        if line.strip() != "":
            numbers.append(line.strip())
    f.close()
    total_number=len(numbers)
    print(style.RED + 'We found ' + str(total_number) + ' numbers in the file' + style.RESET)
    delay = 30

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    print('Once your browser opens up sign in to web whatsapp')
    driver.get('https://web.whatsapp.com')

    answer = askyesno(title='Confirmation',message='Did you scan your whatsapp QR and your chats are visible?') #Confirmation Box to know user scan whatsapp QR or not

# Loop for showing Confirmation box untill the QR is not scan
    while True:
        if answer:
            for idx, number in enumerate(numbers):
                number = number.strip()
                if number == "":
                    continue
                print(style.YELLOW + '{}/{} => Sending message to {}.'.format((idx+1), total_number, number) + style.RESET)
                try:
                    url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
                    sent = False
                    for i in range(3):
                        if not sent:
                            driver.get(url)
                            try:
                                click_btn = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "_1Ae7k")))
                            except Exception as e:
                                print(style.RED + f"\nFailed to send message to: {number}, retry ({i+1}/3)")
                                print("Make sure your phone and computer is connected to the internet.")
                                print("If there is an alert, please dismiss it." + style.RESET)
                            else:
                                sleep(1)
                                click_btn.click()
                                sent=True
                                sleep(3)
                                print(style.GREEN + 'Message sent to: ' + number + style.RESET)
                except Exception as e:
                    print(style.RED + 'Failed to send message to ' + number + str(e) + style.RESET)
            driver.close()
            break

        else:
            answer = askyesno(title='Confirmation',message='Did you scan your whatsapp QR and your chats are visible?')

    
  



root.mainloop()