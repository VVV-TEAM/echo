def bcolors(color):
    colors = {
        "purple": '\033[95m',
        "blue": '\033[94m',
        "cyan": '\033[96m',
        "green": '\033[92m',
        "orange": '\033[93m',
        "red": '\033[91m',
        "classic": '\033[0m',
        "bold": '\033[1m',
        "line": '\033[4m',
    }

    color = color.lower()
    if color in colors:
        return colors[color]
    
    else:
        print(f"Color {color} isn't exist.")
        print()

        return colors["classic"]