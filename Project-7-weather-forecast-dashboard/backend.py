from constants import API_KEY
from geopy.geocoders import Nominatim
import requests
def get_data(place, forecast_days, kind=None):
    geolocator = Nominatim(user_agent="geoapi")
    location = geolocator.geocode(place)

    if not location:
        return {"error": "Invalid city name"}

    lat = location.latitude
    lon = location.longitude

    url = (
        f"https://api.weatherapi.com/v1/forecast.json?key={API_KEY}&days={0}&q={place}"
    )
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    print(get_data("Tokyo",5))


