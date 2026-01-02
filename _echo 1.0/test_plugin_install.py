import json

plugin_name = "test"

plugin_description = {
    "role": "system",
    "content": f"- command: {plugin_name} : print text"
}

def install_plugin():
    print(f"💾 installing {plugin_name} plugin!")
    print()

    print(plugin_description)
    print()

    print("📄 Adding an element to the context")
    print()
    with open("context_generate.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    if data:
        data.append(plugin_description)
        print("📄 Successfully added element to context.")
        print()
    else:
        print("📄 Failed to add element to context.")
        print()

    with open("context_generate.json", "w", encoding="utf-8") as f:
        print("📄 Saving file.")
        print()
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("💣 Installing has been ended")
    print()

    input("click enter: ")

install_plugin()