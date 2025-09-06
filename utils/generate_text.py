import openai
import os
import json

# keys path to json file
with open("./keys.json") as file:
    # json keys file
    data = json.load(file)

# context path to json file
with open("./context_generate.json") as file2:
    # json context file
    context = json.load(file2)

openai_key = data["OpenAi_KEY"]

# This is history of chat
history = []


def generate_response(prompt, information_from_search, weather, time, spotify_stop, spotify_what):
    global history
    global context

    print(f"user question in generate_response: {prompt}")
    print()

    # Add important information to context
    context.append({"role": "system", "content": f"There is what do you need to answer when is None skip this: web_search_information: {information_from_search}, weather {weather}, time {time}, what song now is playing: {spotify_what}, stop music: {spotify_stop}."})

    # Add user message to history
    history.append({"role": "user", "content": prompt})

    # Send system context + history
    messages_to_send = context + history

    print(context)
    print()

    print(history)
    print()

    client = openai.OpenAI(
        api_key=openai_key
    ) 

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages_to_send,
    )

    print(response)
    print()

    ai_message = response.choices[0].message.content

    print(ai_message)
    print()

    # Add assistants reply to history
    history.append({"role": "assistant", "content": ai_message})

    # Keep only the last 5 user messages and 5 assistant answer
    if len(history) > 10:
        history = history[-10:]

    return ai_message