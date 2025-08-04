import os

def clear_terminal():
    # Check the operating system and execute the appropriate clear command
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For Mac and Linux (POSIX systems)
        _ = os.system('clear')