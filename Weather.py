
import tkinter as tk # to build a GUI 
from tkinter import *
from tkinter import ttk # to create a GUI with a theme
import customtkinter as ctk
import requests
from PIL import Image, ImageTk, ImageSequence
from io import BytesIO
from datetime import datetime



def data_get():
    city = city_name.get()
    
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=915848bccd4fa280e71b76aef97bfd46").json()
    
    

    

    w_lable1.config(text = data["weather"][0]["main"])
    wd_lable2.config(text = data["weather"][0]["description"])
    temp_lable3.config(text = str(int(data["main"]["temp"] -273.15 ))+"°C")
    pressure_lable4.config(text = str(int(data["main"]["pressure"]))+"hPa")
    h_lable5.config(text = str(int(data["main"]["humidity"]))+"%")
    ws_lable6.config(text = str(int(data["wind"]["speed"]))+"mph")
    temp_min_lable7.config(text = str(int(data ["main"]["temp_min"] - 273.15 ))+"°C")
    temp_max_lable8.config(text = str(int(data ["main"]["temp_max"] - 273.15 ))+"°C")
    
    
    sunrise_ts = data["sys"]["sunrise"]
    sunset_ts = data["sys"]["sunset"]
    sunrise_time = datetime.fromtimestamp(sunrise_ts).strftime('%H:%M')
    sunset_time = datetime.fromtimestamp(sunset_ts).strftime('%H:%M')
    sr_lable9.config(text = sunrise_time)
    st_lable10.config(text = sunset_time)
 
    lt_lable11.config(text = str(int(data["coord"]["lat"]))+"°")
    lg_lable12.config(text = str(int(data["coord"]["lon"]))+"°")

   
    

win = tk.Tk()
win.title = ("Weather Forcasting")
win.config(bg = "#4E4C4C")
win.geometry("600x1000")

name_lable = tk.Label(win,text = "Weather Forcasting App", font = ("poppins", 22), bg = "white")
name_lable.place(x = 25, y = 50, width= 450)



city_name =StringVar()

list_name =[
    "Agra", "Ahmedabad", "Allahabad", "Amritsar", "Aurangabad",
    "Bangalore", "Bhopal", "Bhubaneswar",
    "Chandigarh", "Chennai", "Coimbatore",
    "Dehradun", "Delhi", "Dhanbad", "Durgapur",
    "Faridabad",
    "Gandhinagar", "Ghaziabad", "Guwahati", "Gwalior",
    "Hyderabad",
    "Indore",
    "Jaipur", "Jalandhar", "Jammu", "Jamshedpur", "Jhansi",
    "Kanpur", "Kochi", "Kolhapur", "Kolkata", "Kozhikode",
    "Lucknow", "Ludhiana",
    "Madurai", "Mangalore", "Meerut", "Mumbai", "Mysore",
    "Nagpur", "Nashik", "Noida",
    "Patna", "Pune",
    "Raipur", "Rajkot", "Ranchi",
    "Shimla", "Siliguri", "Srinagar", "Surat",
    "Thane", "Thiruvananthapuram", "Tiruchirappalli", "Tirunelveli",
    "Udaipur", "Ujjain",
    "Vadodara", "Varanasi", "Vasai-Virar", "Vijayawada", "Visakhapatnam", "Vellore",
    "Warangal"
]


combox = ttk.Combobox(win,text = "Weather Forcasting App",values = list_name , font = ("Open Sans", 10), textvariable = city_name )
combox.place(x = 25, y = 150, width = 450)



w_lable = tk.Label(win,text = "Weather Climate", font = ("Open Sans", 10, "bold"))
w_lable.place(x = 25, y = 260, width= 210)
w_lable1 = tk.Label(win,text = "", font = ("Open Sans", 10,), fg = "gray")
w_lable1.place(x = 250, y = 260, width= 210)

wd_lable = tk.Label(win,text = "Weather Discription", font = ("Open Sans", 10,"bold"))
wd_lable.place(x = 25, y = 300, width= 210)
wd_lable2 = tk.Label(win,text = "", font = ("Open Sans", 10,),fg = "gray")
wd_lable2.place(x = 250, y = 300, width= 210)

temp_lable = tk.Label(win,text = "Temprature", font = ("Open Sans", 10,"bold"))
temp_lable.place(x = 25, y = 340, width= 210)
temp_lable3 = tk.Label(win,text = "", font = ("Open Sans", 10),fg = "gray")
temp_lable3.place(x = 250, y = 340, width= 210)




pressure_lable = tk.Label(win,text = "Pressure", font = ("Open Sans", 10,"bold"))
pressure_lable.place(x = 25, y = 380, width= 210)
pressure_lable4 = tk.Label(win,text = "", font = ("Open Sans", 10),fg = "gray")
pressure_lable4.place(x = 250, y = 380, width= 210)

h_lable = tk.Label(win,text = "Humidity", font = ("Open Sans", 10,"bold"))
h_lable.place(x = 25, y = 420, width= 210)
h_lable5 = tk.Label(win,text = "", font = ("Open Sans", 10),fg = "gray")
h_lable5.place(x = 250, y = 420, width= 210)

ws_lable = tk.Label(win,text = "Wind Speed", font = ("Open Sans", 10,"bold"))
ws_lable.place(x = 25, y = 460, width= 210)
ws_lable6 = tk.Label(win,text = "", font = ("Open Sans", 10),fg = "gray")
ws_lable6.place(x = 250, y = 460, width= 210)

temp_min_lable = tk.Label(win,text = "Min_temp", font = ("Open Sans", 10,"bold"))
temp_min_lable.place(x = 25, y = 500, width= 210)
temp_min_lable7 = tk.Label(win,text = "", font = ("Open Sans", 10),fg = "gray")
temp_min_lable7.place(x = 250, y = 500, width= 210)



temp_max_lable = tk.Label(win,text = "Max_temp", font = ("Open Sans", 10, "bold"))
temp_max_lable.place(x = 25, y = 540, width= 210)
temp_max_lable8 = tk.Label(win,text = "", font = ("Open Sans", 10),fg = "gray")
temp_max_lable8.place(x = 250, y = 540, width= 210)

sr_lable = tk.Label(win,text = "Sun Rise", font = ("Open Sans", 10, "bold"))
sr_lable.place(x = 25, y = 580, width= 210)
sr_lable9 = tk.Label(win,text = "", font = ("Open Sans", 10,), fg = "gray")
sr_lable9.place(x = 250, y = 580, width= 210)

st_lable = tk.Label(win,text = "Sun Set", font = ("Open Sans", 10, "bold"))
st_lable.place(x = 25, y = 620, width= 210)
st_lable10 = tk.Label(win,text = "", font = ("Open Sans", 10,), fg = "gray")
st_lable10.place(x = 250, y = 620, width= 210)

lt_lable = tk.Label(win,text = "Latitude", font = ("Open Sans", 10, "bold"))
lt_lable.place(x = 25, y = 660, width= 210)
lt_lable11 = tk.Label(win,text = "", font = ("Open Sans", 10,), fg = "gray")
lt_lable11.place(x = 250, y = 660, width= 210)

lg_lable = tk.Label(win,text = "Longitude", font = ("Open Sans", 10, "bold"))
lg_lable.place(x = 25, y = 700, width= 210)
lg_lable12 = tk.Label(win,text = "", font = ("Open Sans", 10,), fg = "gray")
lg_lable12.place(x = 250, y = 700, width= 210)

f_lable = tk.Label(win,text = "", font = ("Open Sans", 10, "bold"))
f_lable.place(x = 25, y = 740, width= 435, height= 100)


button = ctk.CTkButton(win, text="Done", font = ("roboto", 20), command=data_get,height = 40, width= 140,  corner_radius=20, fg_color="white", text_color="Black", border_color="black", border_width=2)
button.place(y = 190,  x = 170)
win.mainloop()





# https://pro.openweathermap.org/data/2.5/forecast/climate?q={city name},{country code}&appid=915848bccd4fa280e71b76aef97bfd46

