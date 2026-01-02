from datetime import datetime
from zoneinfo import ZoneInfo

# Get time from country
def get_time(country):
    country_to_tz = {
        "poland": "Europe/Warsaw",
        "germany": "Europe/Berlin",
        "france": "Europe/Paris",
        "spain": "Europe/Madrid",
        "italy": "Europe/Rome",
        "uk": "Europe/London",
        "united kingdom": "Europe/London",
        "usa": "America/New_York",  
        "united states": "America/New_York",
        "canada": "America/Toronto",
        "brazil": "America/Sao_Paulo",
        "argentina": "America/Argentina/Buenos_Aires",
        "mexico": "America/Mexico_City",
        "russia": "Europe/Moscow",  
        "china": "Asia/Shanghai",
        "japan": "Asia/Tokyo",
        "south korea": "Asia/Seoul",
        "india": "Asia/Kolkata",
        "australia": "Australia/Sydney",
        "egypt": "Africa/Cairo",
        "south africa": "Africa/Johannesburg",
    }

    print(country)

    if not country:
        return "No country provided"

    country = country.lower()
    if country in country_to_tz:
        tz = ZoneInfo(country_to_tz[country])
        now = datetime.now(tz)

        time = now.strftime("%Y-%m-%d %H:%M:%S")

        time = f"Current time in {country} is {time}"
        return time
    
    else:
        return f"I can't see time for {country}"