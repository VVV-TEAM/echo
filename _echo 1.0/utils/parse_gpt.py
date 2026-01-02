import re

def parse_gpt_response(gpt_response: str) -> dict:
    text = gpt_response.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z0-9_+-]*\s*|\s*```$", "", text, flags=re.DOTALL).strip()

    parsed_data = {
        "response": None,
        "write_discord": None,
        "remember": None,
        "channel_id": None,
        "spotify_play_music": None,
        "spotify_resume": None,
        "spotify_previous_song": None,
        "spotify_set_volume": None,
        "spotify_next_song": None,
        "command_found": False,
        "plugins": []
    }

    line_kv = re.compile(r'(?m)^\s*([a-zA-Z_][\w-]*)\s*:\s*(.+?)\s*$')

    for raw_key, raw_val in line_kv.findall(text):
        key = raw_key.strip().lower().replace('-', '_') 
        val = raw_val.strip()

        # skip none
        if not val or val.lower() == 'none':
            continue

        if key == "response":
            parsed_data["response"] = val
            continue

        if key in {
            "write_discord",
            "remember",
            "channel_id",
            "spotify_play_music",
            "spotify_resume",
            "spotify_previous_song",
            "spotify_set_volume",
            "spotify_next_song",
        }:
            parsed_data[key] = val
            parsed_data["command_found"] = True
        else:
            # plugins and command not found
            parsed_data["plugins"].append({"command": key, "args": val})
            parsed_data["command_found"] = True

    if parsed_data["channel_id"] and not parsed_data["command_found"]:
        parsed_data["command_found"] = True

    return parsed_data
