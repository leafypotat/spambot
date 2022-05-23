import pyautogui, time
def start():
    choice = input("Paste from the text-file or clipboard (t/c)")
    if choice == "t":
        confimation = input("Are you sure? (Y/N)")
        if confimation == "y" or confirmation == "Y":
            time.sleep(5)
            file = open("spambot.txt", 'r')
            for word in file:
                pyautogui.typewrite(word)
                pyautogui.press("enter")
        else:
            start()

    elif choice == "c":
        confimation = input("Are you sure? (Y/N)")
        if confimation == "y" or confirmation == "Y":
            print_num = int(input("How many times should it be printed?"))
            print("Time delay of 7 seconds.....")
            time.sleep(7)
            for n in range(print_num):
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(0.25)
                pyautogui.press('enter')
        else:
            start()

    else:
        print("Invalid option")
        start()

start()
