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




root=Tk()
root.iconbitmap('window.ico')
root.geometry('750x550')
root.title('Whatsapp')
f = font.Font(family='System', size=14, weight="bold")
fNum = font.Font(family='System', size=10)


def upload_file():
    f_types = [("xlxs files", ".*xlsx")]   # type of files to select 
    filename = tk.filedialog.askopenfilename(multiple=False,filetypes=f_types)
    f = r"{}".format(filename)
    df = pd.read_excel(filename)
    numbers=df.Number

    txt=''
    counter=1
    for i in numbers:
        txt=txt+'('+str(counter)+')    '+'+'+str(i)+'\n'
        counter=counter+1
    
    numbersList.config(text=txt)
    with open("numbers.txt","w") as nFile:
        nFile.write(txt)


def start():
    pass








l1 = Label(root, text = "Upload Excel File",font=f)
l1.grid(row = 0, column = 0, sticky = W, pady = 10,padx=15)

fileUpload = Button(root, text="Upload File",command=upload_file)
fileUpload.grid(row=1, column=0)


l1 = Label(root, text = "Message",font=f)
l1.grid(row = 2, column = 0, sticky = W,padx=15)

area = Text(root,width='40',height='20')
area.grid(row=3, column=0,
padx=15,pady=10, sticky=E+W+S+N)

startbtn = Button(root, text="Start",command=start)
startbtn.grid(row=4, column=0)


numbersHeading = Label(root, text="Numbers",font=f)
numbersHeading.grid(row=0,column=4,padx=20)


numbersList = Label(root, text="")
numbersList.grid(row=2,column=4,padx=30)






root.mainloop()