import re

def parse_gpt_response2(gpt_response: str) -> dict:
    text = gpt_response.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z0-9_+-]*\s*|\s*```$", "", text, flags=re.DOTALL).strip()

    parsed_data = {
        "search": None,
        "weather": None,
        "spotify_stop": None,
        "spotify_what_music": None,
        "time": None,
        "command_found": False
    }

    line_kv = re.compile(r'(?m)^\s*([a-zA-Z_][\w-]*)\s*:\s*(.+?)\s*$')

    for raw_key, raw_val in line_kv.findall(text):
        key = raw_key.strip().lower().replace('-', '_')
        val = raw_val.strip()

        # skip none
        if not val or val.lower() == "none":
            continue

        if key in parsed_data:
            parsed_data[key] = val
            parsed_data["command_found"] = True

    return parsed_data
