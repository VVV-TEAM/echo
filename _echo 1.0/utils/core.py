from utils.generate_text import generate_response
from utils.speak import speak
from utils.generate_tts import generate_tts
from utils.parse_gpt import parse_gpt_response
from utils.parse_gpt2 import parse_gpt_response2
from utils.first_look_answer import first_look_for_answer
from utils.exa_api import web_search
from utils.parse_weather_code import weather_code
from utils.plugin_manager import load_plugins, plugins
from utils.bcolors import bcolors
from assistants.discord_write import write_discord
from assistants.time import get_time
from assistants.weather import get_coordinates, get_weather
from assistants.spotify import search_music, choice_devices, play_music, stop_play, start_play, next_song, previous_song, set_volume, what_play

def core(user_input, plugins):
    classic = bcolors(color="classic")

    if user_input:
        information_from_search = None
        weather = None
        time = None
        spotify_stop = None
        spotify_what = None

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
            
            if parsed_data_2.get("search") is not None:
                print(f"I need to search: {parsed_data_2['search']}")
                print()

                information_from_search = web_search(parsed_data_2['search'])

                blue = bcolors(color="blue")

                print(f"{blue} {information_from_search} {classic}")
                print()

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

                        blue = bcolors(color="blue")

                        weather = [
                            f"Weather for {city_name}, {country} "
                            f"temperature: {temperature} °C "
                            f"windspeed: {windspeed} km/h "
                            f"weather: {what_weather} "
                        ]

                        print(f"{blue} {weather} {classic}")
                        print()

                    else:
                        weather = "I can't see information about weather"

                        orange = bcolors(color="orange")

                        print(f"{orange} I can't see information about weather {classic}")
                        print()

                else:
                    weather = "I can't see information about weather"

                    orange = bcolors(color="orange")

                    print(f"{orange} I can't see coords {classic}")
                    print()



            elif parsed_data_2["time"]:
                print(f"I need to know what time is it")
                print()

                time = get_time(parsed_data_2['time'])

                blue = bcolors(color="blue")

                print(f"{blue} {time} {classic}")
                print()

            elif parsed_data_2["spotify_stop"] is not None:
                print("I need stop music from spotify")
                print()
                device_id = choice_devices()
                stop_play(device_id)

                blue = bcolors(color="blue")

                print(f"{blue} The music has stopped {classic}")
                print()

                spotify_stop = "You are stop music"

            elif parsed_data_2["spotify_what_music"] is not None:
                print("I need now what music is now playing")
                print()

                spotify_what = what_play()

                blue = bcolors(color="blue")

                print(f"{blue} {spotify_what} {classic}")
                print()

            gpt_response = generate_response(prompt, information_from_search, weather, time, spotify_stop, spotify_what)
            blue = bcolors(color="blue")
            print(f"🤖 {blue}Echo: {gpt_response} {classic}")
            print()

            parsed_data = parse_gpt_response(gpt_response)

            if parsed_data["response"]:
                response = parsed_data["response"]
                generate_tts(response)
                speak()
            
            if parsed_data["command_found"]:
                if parsed_data["write_discord"] is not None:
                    if parsed_data["channel_id"] is not None:
                        print(f"I send message: {blue}'{parsed_data['write_discord']}'{classic} to channel id: {blue}{parsed_data['channel_id']}{classic}")
                        print()
                        write_discord(parsed_data["write_discord"], parsed_data["channel_id"])
                    else:
                        red = bcolors(color="red")
                        print(f"{red}ERROR: I didn't see channel_id to send message on discord.{classic}")
                        print()
            
                elif parsed_data["spotify_play_music"] is not None:
                    spotify_search = search_music(parsed_data["spotify_play_music"])

                    print(parsed_data["spotify_play_music"])
                    print()

                    device_id = choice_devices()
                    play_music(device_id, spotify_search)

                elif parsed_data["spotify_resume"] is not None:
                    device_id = choice_devices()
                    start_play(device_id)

                elif parsed_data["spotify_next_song"] is not None:
                    device_id = choice_devices()
                    next_song(device_id)

                elif parsed_data["spotify_previous_song"] is not None:
                    device_id = choice_devices()
                    previous_song(device_id)

                elif parsed_data["spotify_set_volume"] is not None:
                    device_id = choice_devices
                    set_volume(parsed_data["spotify_set_volume"], device_id)

            for plugin_cmd in parsed_data["plugins"]:
                cmd = plugin_cmd["command"]
                args = plugin_cmd["args"]

                if cmd in plugins:
                    green = bcolors(color="green")
                    print(f"🔌 {green}Running{classic} plugin {blue}{cmd}{classic} with args: {blue}{args}{classic}")
                    plugins[cmd].run(cmd, args, response)
                else:
                    red = bcolors(color="red")
                    print(f"{red}ERROR: I didn't see plugin {blue}{cmd}{classic}")