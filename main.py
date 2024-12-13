from owm_key import owm_api_key
import requests


def get_weather_now(place, api_key=None):
    params = {"q": place, "appid": api_key, "units": "metric", "lang": "ru"}
    r = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
    result = r.json()
    print(result)


def get_weather_forecast(place, api_key=None):
    params = {"q": place, "appid": api_key, "units": "metric", "lang": "ru"}
    r = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=params)
    result = r.json()
    print(result)


if __name__ == '__main__':
    get_weather_now('Moscow', api_key=owm_api_key)
    get_weather_forecast('Moscow', api_key=owm_api_key)
