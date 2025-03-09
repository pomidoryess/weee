import requests
import sqlite3
from datetime import datetime

# короче луцьк гамно, тому буде житомир, я не знаю норм сайтів з погодою, тому взяв https://openweathermap.org, на ньому тре взяти апі, мені цим в падлу маятись
API_KEY = 'тут має бути код апі'
CITY = 'Zhytomyr,UA'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'
def temp():
    response = requests.get(URL)
    data = response.json()
    if response.status_code == 200:
        temperature = data['main']['temp']
        return temperature
    else:
        print(f"хз помилка якась: {data['message']}")
        return None

def create_table():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            datetime TEXT,
            temperature REAL)''')
    conn.commit()
    conn.close()
def hzneprudymav(temperature):
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''INSERT INTO weather_data (datetime, temperature)VALUES (?, ?)''', (now, temperature))
    conn.commit()
    conn.close()
create_table()
temperature = get_current_temperature()
if temperature is not None:
    insert_data(temperature)
    print(f"👍: {temperature}°C на {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
else:
    print("помилка лололо.")
