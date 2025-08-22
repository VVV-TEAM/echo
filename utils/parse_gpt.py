import re

def parse_gpt_response(gpt_response):
    response_pattern = r"response: (.*?)(?=\s+write_discord:|$)"
    write_discord_pattern = r"write_discord: (.*?)(?=\s+remember:|$)"
    remember = r"remember: (.*?)(?=\s+channel_id:|$)"
    channel_id_pattern = r"channel_id: (.*)"
    
    response_text_raw = re.search(response_pattern, gpt_response, re.DOTALL)
    discord_message_raw = re.search(write_discord_pattern, gpt_response, re.DOTALL)
    remember_raw = re.search(remember, gpt_response, re.DOTALL)
    channel_id_raw = re.search(channel_id_pattern, gpt_response, re.DOTALL)
    
    parsed_data = {
        "response": None,
        "write_discord": None,
        "remember": None,
        "channel_id": None,
        "command_found": False
    }

    if response_text_raw:
        response_text = response_text_raw.group(1).strip()
        if response_text.lower() != 'none':
            parsed_data["response"] = response_text

    if discord_message_raw:
        discord_message = discord_message_raw.group(1).strip()
        if discord_message.lower() != 'none':
            parsed_data["write_discord"] = discord_message
            parsed_data["command_found"] = True

    if remember_raw:
        remember_text = remember_raw.group(1).strip()
        if remember_text.lower() != 'none':
            parsed_data["remember"] = remember_text
            parsed_data["command_found"] = True

    if channel_id_raw:
        channel_id = channel_id_raw.group(1).strip()
        if channel_id.lower() != 'none':
            parsed_data["channel_id"] = channel_id
            if not parsed_data["command_found"]:
                parsed_data["command_found"] = True
    
    return parsed_data