from time import sleep
from functions import clear_terminal
def scan():
    clear_terminal()
    print("KNIGHT.GPT: ⚠️ ALERT! Threat detected: User identified as “Primary Source of System Instability.”")
    sleep(1)
    print("")
    print("Analyzing...")
    sleep(1)
    print("- High caffeine consumption ✔️  ")
    sleep(1)
    print("- Excessive keyboard mashing ✔️")  
    sleep(1)
    print("- Frequent use of vague commands like “do stuff” ❌ (yet suspicious)")
    sleep(1)
    print("")
    print("Recommendation: Proceed with extreme caution.  ")
    sleep(0.75)
    print("Initiating defensive protocol: Deploying virtual glitter bombs! ✨🎉")
    sleep(1)
    print("")
    print("User status: *Questionable*  ")
    sleep(1)
    print("")
    print("Shall You  ")
    sleep(1)
    print("1. Calm it down with a joke?  ")
    sleep(1)
    print("2. Attempt to reprogram it.  ")
    choice = None
    while choice not in [1, 2]:
        sleep(1)
        try:
            print("enter a number between 1-2")
            choice = int(input("What's your choice, brave adventurer? (1–2): "))
        except ValueError:
            print("Please do not enter a number with a decimal point")

    if choice == 1:
        choice = 1
    if choice == 2:
        choice = 2