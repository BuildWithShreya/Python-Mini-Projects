import json
import requests
from win10toast import ToastNotifier
import time

def update():
    try:
        r = requests.get('https://disease.sh/v3/covid-19/all')
        r.raise_for_status()  # Check if the request was successful
        data = r.json()
        text = f'Confirmed Cases: {data["cases"]} \nDeaths: {data["deaths"]} \nRecovered: {data["recovered"]}'
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return
    except json.JSONDecodeError:
        print("Failed to decode JSON response")
        return

    toast = ToastNotifier()
    while True:
        toast.show_toast("Covid-19 Updates", text, duration=20)
        time.sleep(60)

update()
