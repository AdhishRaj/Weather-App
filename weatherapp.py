import tkinter as tk
import requests

HEIGHT = 500
WIDTH = 600

# def test_function(entry):
#     print("This is the entry", entry)

# 09ea7d371a7ce0e415b07fbbe05ed827
    # 81cc64ebb7c3947611746f08d1b8ca5d
# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}

def format_response(weather):
    try:
        name = weather['name']
        country = weather['sys']['country']
        desc = weather['weather'][0]['description'] 
        temp = weather['main']['temp']

        final_str = 'City: %s \nCountry: %s \nConditions: %s \nTemperature (°C): %s' %(name, country, desc, temp)
    except:
        final_str = "Incorrect entry"

    return final_str

def get_weather(city):
    weather_key = '09ea7d371a7ce0e415b07fbbe05ed827'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q':city, 'units':'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

bg_img = tk.PhotoImage(file="weather.png")
bg_label = tk.Label(root, image=bg_img)
bg_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.75, anchor='n')

button = tk.Button(frame, text='Get Weather', font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=40, anchor = 'nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()