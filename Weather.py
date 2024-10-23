

"""Dheeraj Naik, Project: Weather App"""


import tkinter as tk
from PIL import Image, ImageTk
import requests
import time

#get data from api
def getWeather(canvas):
    city=textfield.get()
    api="https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=3e3478877717792204f0cfcd5fe207aa"
    json_data=requests.get(api).json()
    condition=json_data['weather'][0]['main']
    temp=int(json_data['main']['temp'] - 273.15)
    min_temp=int(json_data['main']['temp_min'] - 273.15)
    max_temp=int(json_data['main']['temp_max'] - 273.15)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    wind=json_data['wind']['speed']
    sunrise=time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset=time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset'] - 21600))
    
    last_info= condition + " " + str(temp) + "°C"
    last_data= "Max Temp : " +str(max_temp) + "°C" + " to " + "Min Temp : " +str(min_temp) + "°C" + "\n" + "Pressure : " +str(pressure) + "\n" + "Humidity : " +str(humidity) + "\n" + "Wind Speed : " +str(wind) + "\n" + "Sunrise : " +sunrise + " to " + "Sunset : " +sunset 
    label1.config(text=last_info)
    label2.config(text=last_data)
    
    
canvas = tk.Tk()
canvas.geometry("600x350")
canvas.title("weather app")

bg_image = Image.open("sky.jpg")  # Make sure the image is in the same directory or provide the correct path
bg_image = bg_image.resize((600, 350), Image.ANTIALIAS)  # Resize image to fit the window
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(canvas, image=bg_photo)
bg_label.place(relwidth=1, relheight=1) 

f = ("Arial", 15, "bold")
t = ("Arial", 35, "bold")

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>',getWeather)     #return value obtained from textfield to getWeather function.

label1=tk.Label(canvas,font=t)
label1.pack()

label2=tk.Label(canvas,font=f)
label2.pack()

canvas.mainloop()

