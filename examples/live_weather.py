#Description
#This is a program which collects real time weather data from openweathermap.org 
#It uses rxpy to then filter and give required information to the subscribers using filters

 

import rx
from rx import operators as ops
import json,requests,time
from datetime import datetime
from rx.subject import ReplaySubject,BehaviorSubject
import threading

#variables
API_KEY = "36c140b1321fdedc00e3015b028aae5f"
LOCATION = "bangalore"
API_CALL = "https://api.openweathermap.org/data/2.5/weather?q="+LOCATION+"&appid="+API_KEY
REPLAY = 10


#get weather function
def get_weather():
    global API_CALL
    data = requests.get(API_CALL).json()
    if data['cod'] == "404":
        pass
    else:
        weather_info = {"time":datetime.now().strftime("%H:%M:%S"),"temp":"{:.1f}".format(data['main']['temp'] - 273.15),"description":data['weather'][0]['description']}
        return weather_info
    return None

#write info to json file function
def jsonwrite():
    global LOCATION
    while True:
        time.sleep(2)
        weather_info = get_weather()
        if weather_info == None:
            break
        else :
            try:
                with open("weather.json") as file:
                    old_data = json.load(file)
            except :
                old_data = {}
                old_data[LOCATION] = {"time":[weather_info["time"]],"temp":[weather_info["temp"]],"description":[weather_info["description"]]}
                with open("weather.json","w") as file:
                    json.dump(old_data,file,indent=4)
            else:
                if LOCATION in old_data:
                    old_data[LOCATION]['time'].append(weather_info['time'])
                    old_data[LOCATION]['temp'].append(weather_info['temp'])
                    old_data[LOCATION]['description'].append(weather_info['description'])
                    with open("weather.json","w") as file:
                        json.dump(old_data,file,indent=4)            
                else :
                    old_data[LOCATION] = {"time":[weather_info["time"]],"temp":[weather_info["temp"]],"description":[weather_info["description"]]}
                    with open("weather.json","w") as file:
                        json.dump(old_data,file,indent=4)   
    
    return None

threading.Thread(target=jsonwrite).start()

subject = ReplaySubject(REPLAY)
def subjectt():
    global subject
    while True:
        time.sleep(5)
        with open("weather.json") as file:
            data = json.load(file)
        data = data[LOCATION]
        subject.on_next(data)
threading.Thread(target=subjectt).start()
subject.pipe(
    ops.filter(lambda s: float(s['temp'][-1]) > 2)
).subscribe(
    lambda s:print("1- At {} it was {} degree celcius".format(s['time'][-1],s['temp'][-1]))
)

print("Using Threads:",threading.active_count())

    