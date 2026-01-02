import os
import importlib
import sys

plugins = {}

def load_plugins():
    folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "plugins")
    
    print("Search folder plugins")
    print()
    for file in os.listdir(folder):
        print("Looking for plugins")
        print()
        if file.endswith(".py"):
            module_name = f"plugins.{file[:-3]}"
            module = importlib.import_module(module_name)

            for cmd in getattr(module, "commands", []):
                plugins[cmd] = module

    print(f"🔌 Loaded plugins: {list(plugins.keys())}")
    print()