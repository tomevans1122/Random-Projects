import tkinter as tk
from tkinter import font
import requests
from PIL import Image, ImageTk

HEIGHT = 700
WIDTH = 800

def test_function(entry):
	print("This is the entry:", entry)

# cece23f81688b90fe5032d36ca6e2008
# api.openweathermap.org/data/2.5/forecast?q={city name},{state code},{country code}&appid={your api key}
def format_response(weather):
	try:
		name = weather['name']
		desc = (weather['weather'][0]['description'])
		temp = (weather['main']['temp'])

		final_str = f"City: {name} \nCondition: {desc} \nTemperature: {temp}°C"
	except:
		final_str = "There was a problem retrieving that information" 

	return final_str


def get_weather(city):
	weather_key = 'cece23f81688b90fe5032d36ca6e2008'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
	response = requests.get(url, params = params)
	print(response.json())
	weather = response.json()

	label['text'] = format_response(weather)


root = tk.Tk() #creates widget

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file = 'landscape.png')
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

frame = tk.Frame(root, bg = '#80c1ff', bd = 5) 
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor ='n')

entry = tk.Entry(frame, font = ('Courier', 12))
entry.place(relwidth = 0.65, relheight = 1)

button = tk.Button(frame, text = 'Get Weather', font = ('Courier', 12), command = lambda: get_weather(entry.get()))
button.place(relx = 0.7, relheight = 1, relwidth = 0.3)

lower_frame = tk.Frame(root, bg = '#80c1ff', bd = 10)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = 'n') 


label = tk.Label(lower_frame, font = ('Courier', 18), anchor = 'nw', justify = 'left', bd = 4)
label.place(relwidth = 1, relheight = 1)

root.mainloop(0) #opens widget


