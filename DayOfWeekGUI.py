# Script provides the day of week of any date in history or the future via GUI.

import tkinter as tk
from tkinter import font
import requests
import math
import calendar
import datetime 
from datetime import datetime 


#Gregorian calendar month codes- changed from julian calendar in 1752
centuryCode = {17:4, 18:2, 19:0, 20:6, 21:4, 22:2, 23:0, 24:6, 25:4, 26:2, 27:0}

#dictionary for month code
monthCode = {1:0, 2:3, 3:3, 4:6, 5:1, 6:4, 7:6, 8:2, 9:5, 10:0, 11:3, 12:5}

#dictionary for days of the week
daysCode = {0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}

def year_code(year):
    return (year + math.floor(year/4)) % 7

def century_code(century):
    if century < 17:
        return (18 - century) % 7
    else:
        return centuryCode[century]

def leap_check(full_year, month):
    leap = calendar.isleap(full_year)
    if leap and month == 1:
        return -1
    elif leap and month == 2:
        return -1
    else:
        return 0 


def final_answer(result):
    string_input_with_date = entry.get() + "/" + entry1.get() + "/" + entry2.get()
    given_date = datetime.strptime(string_input_with_date, "%d/%m/%Y")
    present = datetime.now()

    if present >= given_date:                                                      
        label['text'] = f"That date fell on a {daysCode[result]}"
    else:
        label['text'] = f"That date falls on a {daysCode[result]}"   



    
def day_of_week(num1, num2, num3):
    # turn string input into int
    day = int(entry.get())
    month = int(entry1.get())
    full_year = int(entry2.get())
    full_year_str = entry2.get()
    year = int(full_year_str[2:])
    century = int(full_year_str[:2])

    # convert times to 
    #string_input_with_date = entry.get() + "/" + entry1.get() + "/" + entry2.get()
    #given_date = datetime.strptime(string_input_with_date, "%d/%m/%Y")
    #present = datetime.now()

    result = (year_code(year) + monthCode[month] + century_code(century) + day - leap_check(full_year, month)) % 7

    label['text'] = final_answer(result)
    


        
HEIGHT = 800
WIDTH = 700

root = tk.Tk()     #creates widget

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH, bg = '#54a8f7')
canvas.pack()

background_image = tk.PhotoImage(file = 'blueBack.png')
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

########################## FIRST ENTRY ####################
frame = tk.Frame(root, bg = '#54A8F7', bd = 3) 
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor ='n')

entry = tk.Entry(frame, font = ('Courier', 10), justify = 'center')
entry.place(relwidth = 0.65, relheight = 0.8)

label1 = tk.Label(entry, font = ('Courier', 9), text = 'Please enter a day of the month (e.g. 1, 24):', anchor = 'n', justify = 'left', bd = 1, bg = 'white')
label1.place(relwidth = 1, relheight = 0.4)


########################## SECOND ENTRY #################
frame1 = tk.Frame(root, bg = '#54A8F7', bd = 3) 
frame1.place(relx = 0.5, rely = 0.2, relwidth = 0.75, relheight = 0.1, anchor ='n')

entry1 = tk.Entry(frame1, font = ('Courier', 10), justify = 'center')
entry1.place(relwidth = 0.65, relheight = 0.8)

label2 = tk.Label(entry1, font = ('Courier', 9), text = 'Please enter a month of the year (e.g. 3, 12):', anchor = 'n', justify = 'left', bd = 1, bg = 'white')
label2.place(relwidth = 1, relheight = 0.4)

######################### THIRD ENTRY #######################
frame2 = tk.Frame(root, bg = '#54A8F7', bd = 3) 
frame2.place(relx = 0.5, rely = 0.3, relwidth = 0.75, relheight = 0.1, anchor ='n')

entry2 = tk.Entry(frame2, font = ('Courier', 10), justify = 'center')
entry2.place(relwidth = 0.65, relheight = 0.8)

label3 = tk.Label(entry2, font = ('Courier', 9), text = 'Please enter any year in full (e.g. 1996):', anchor = 'n', justify = 'left', bd = 1, bg = 'white')
label3.place(relwidth = 1, relheight = 0.4)


######### CALCULATE BUTTON ##########
button = tk.Button(frame1, text = 'Calculate', font = ('Courier', 8), command = lambda: day_of_week(entry.get(),entry1.get(),entry2.get()))
button.place(relx = 0.68, relheight = 0.8, relwidth = 0.3)


##### ANSWER BOX ########
lower_frame = tk.Frame(root, bg = '#80c1ff', bd = 10)
lower_frame.place(relx = 0.5, rely = 0.4, relwidth = 0.75, relheight = 0.5, anchor = 'n') 


label = tk.Label(lower_frame, font = ('Courier', 18), anchor = 'nw', justify = 'left', bd = 4)
label.place(relwidth = 1, relheight = 1)





root.mainloop(0)
