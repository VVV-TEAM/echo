import re

def parse_gpt_response2(gpt_response):
    search_pattern = r"search: (.*?)(?=\s+weather:|$)"
    weather_pattern = r"weather: (.*?)(?=\s+time:|$)"
    time_pattern = r"time: (.*)"
    
    search_text_raw = re.search(search_pattern, gpt_response, re.DOTALL)
    weather_raw = re.search(weather_pattern, gpt_response, re.DOTALL)
    time_raw = re.search(time_pattern, gpt_response, re.DOTALL)
    
    parsed_data = {
        "search": None,
        "weather": None,
        "time": None,
        "command_found": False
    }

    if search_text_raw:
        search_text = search_text_raw.group(1).strip()
        if search_text.lower() != 'none':
            parsed_data["search"] = search_text

    if weather_raw:
        weather = weather_raw.group(1).strip()
        if weather.lower() != 'none':
            parsed_data["weather"] = weather

    if time_raw:
        channel_id = time_raw.group(1).strip()
        if channel_id.lower() != 'none':
            parsed_data["time"] = channel_id
    
    return parsed_data