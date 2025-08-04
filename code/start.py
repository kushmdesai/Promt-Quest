import time
print("SYSTEM STATUS: BOOT COMPLETE.")
print("Welcome, Prompt Engineer #404.")
time.sleep(1)
print("")
print("Your AI assistant, Codename: KNIGHT.GPT, is waking up after 1000 years of standby.")
time.sleep(1)
print("")
print("ERROR: All mission parameters corrupted.")
print("Your task: Guide it through a broken world using only prompts.")
time.sleep(1)
print("")
print("⚠️ WARNING: The AI interprets prompts... creatively.")
time.sleep(1)
print("")
print("You have 3 choices")
time.sleep(1)
print("")
print("1. wake up and scan for threats")
time.sleep(1)
print("2. introduce yourself to the nearest lifeform")
time.sleep(1)
print("3. build sentient toaster first, THEN assess situation")
choice = None
while choice not in [1, 2, 3]:
    time.sleep(1)
    try:
        print("enter a number between 1-3")
        choice = int(input("What's your choice, brave adventurer? (1–3): "))
    except ValueError:
        print("Please do not enter a number with a decimal point")

