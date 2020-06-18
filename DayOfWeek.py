import tkinter as tk
from tkinter import font
import requests
import math


# Given any date in the style XX/X/XXXX, figure out the day of the week of that date


day_input = input("Please provide any day of a month (e.g. 2, 24): ")
month_input = input("Please provide any month of the year (e.g. 3, 12): ")
full_year_input = input("Please provide any year in the format XXXX: ")

day = int(day_input)
month = int(month_input)
full_year = int(full_year_input)
year = int(full_year_input[2:])
century = int(full_year_input[:2])

#Gregorian calendar month codes- changed from julian calendar in 1752
century_code = {17:4, 18:2, 19:0, 20:6, 21:4, 22:2, 23:0, 24:6, 25:4, 26:2, 27:0}

#dictionary for month code
month_code = {1:0, 2:3, 3:3, 4:6, 5:1, 6:4, 7:6, 8:2, 9:5, 10:0, 11:3, 12:5}

#dictionary for days of the week
days = {0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}


class Codes:

	def __init__(self, year, month, century):
		self.year = year
		self.month = month
		self.century = century

	def year_code(self, year):
		return (year + math.floor(year/4)) % 7

	def month_code(self, month):
		return month_code[month]

	def century_code(self, century):
		if century < 17:
			return (18-century) % 7 #accounts for julian dates (0000's to 1700's)
		else:
			return century_code[century]

	def leap_year(self, full_year, century):
		if century >= 17 and full_year % 4 == 0 and full_year % 100 != 0 and full_year % 400 == 0 and month == 1 or month == 2:
			return -1
		elif century < 17 and full_year % 4 == 0:
			return -1
		else:
			return 0

# Assigning a variable to the class
func = Codes(year, month, century)

# function for formula of calculating the day of the week, leap year or not
def day_of_week(func):
		return (func.year_code(year) + func.month_code(month) + func.century_code(century) + day - func.leap_year(full_year, century)) % 7

number = day_of_week(func)

#final answer
def final_answer(number):
	if full_year < 2020:
		print(f"This date fell on a {days[number]}.")
	else:
		print(f"This date will fall on a {days[number]}.")



day_of_week(func)  
final_answer(number) 
