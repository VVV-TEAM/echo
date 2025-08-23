# imports
from utils.voice_input import listen
from utils.generate_text import generate_response
from utils.speak import speak
from utils.generate_tts import generate_tts
from utils.parse_gpt import parse_gpt_response
from utils.parse_gpt2 import parse_gpt_response2
from utils.first_look_answer import first_look_for_answer
from utils.exa_api import web_search
from utils.parse_weather_code import weather_code
from assistants.discord_write import write_discord
from assistants.time import get_time
from assistants.weather import get_coordinates, get_weather


# Main while
while True:
    user_input = listen()

    if any(trigger in user_input for trigger in ["echo"]):
        
        information_from_search = None
        weather = None
        time = None
        
        if user_input.strip() in ["echo"]:
            continue

        prompt = user_input
        if prompt:
            first_look = first_look_for_answer(prompt)
            print(f"♾️ First Look: {first_look}")
            print()

            parsed_data_2 = parse_gpt_response2(first_look)

            print(parsed_data_2)
            print(parsed_data_2["search"])
            print(parsed_data_2["weather"])
            print(parsed_data_2["time"])
            print()
            
            if parsed_data_2["search"]:
                print(f"I need to search: {parsed_data_2['search']}")
                print()
                information_from_search = web_search(parsed_data_2['search'])

            elif parsed_data_2["weather"]:
                print(f"I need to know weather in {parsed_data_2['weather']}")
                print()
                coords = get_coordinates(parsed_data_2['weather'])
                
                print(coords)
                print()

                if coords:
                    lat, lon, city_name, country = coords

                    print(lat)
                    print(lon)
                    print(city_name)
                    print(country)
                    print()

                    weather_info = get_weather(lat, lon)
                    print(weather_info)
                    print()

                    if weather_info:
                        temperature = weather_info['temperature']
                        windspeed = weather_info['windspeed']
                        weathercode = weather_info['weathercode']

                        what_weather = weather_code(weathercode)

                        weather = [
                            f"Weather for {city_name}, {country}"
                            f"temperature: {temperature} °C"
                            f"windspeed: {windspeed} km/h"
                            f"weather: {what_weather}"
                        ]

                        print(weather)
                        print()

                    else:
                        weather = "I can't see information about weather"
                else:
                    weather = "I can't see information about weather"



            elif parsed_data_2["time"]:
                print(f"I need to know what time is it")
                print()

                time = get_time(parsed_data_2['time'])

                print(time)
                print()
                


            gpt_response = generate_response(prompt, information_from_search, weather, time)
            print(f"🤖 Echo: {gpt_response}")
            print()

            parsed_data = parse_gpt_response(gpt_response)

            if parsed_data["response"]:
                generate_tts(parsed_data["response"])
                speak()
            
            if parsed_data["command_found"]:
                if parsed_data["write_discord"] is not None:
                    if parsed_data["channel_id"] is not None:
                        print(f"I send message: '{parsed_data['write_discord']}' to channel id: {parsed_data['channel_id']}")
                        print()
                        write_discord(parsed_data["write_discord"], parsed_data["channel_id"])
                    else:
                        print("ERROR: I didn't see channel_id to send message on discord.")
                        print()
            
    else:
        continue