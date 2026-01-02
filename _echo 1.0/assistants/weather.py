import requests

# get coords of city
def get_coordinates(city: str):
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    response = requests.get(geo_url)

    if response.status_code == 200:
        data = response.json()
        if data.get("results"):
            result = data["results"][0]
            return (
                result["latitude"],
                result["longitude"],
                result["name"],
                result.get("country", "")
            )
    return None


# Get weather from coords
def get_weather(latitude: float, longitude: float):
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(weather_url)

    if response.status_code == 200:
        data = response.json()
        return data.get("current_weather")
    return None
