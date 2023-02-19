import pyautogui
import tkinter as tk

def click_and_type(text):
    # get the current mouse position
    x, y = pyautogui.position()
    # click a specified location on the screen
    pyautogui.click(3700, 960)
    # type the specified command
    pyautogui.typewrite(text)
    # press the Enter key
    pyautogui.press('enter')
    # return the mouse to the button
    pyautogui.moveTo(x, y)

# Create the GUI
root = tk.Tk()
root.title("Button Clicker")
root.geometry("200x400")

# Define the buttons
button1 = tk.Button(root, text="!battleroyale", command=lambda: click_and_type("!battleroyale"))
button2 = tk.Button(root, text="!gauntlet", command=lambda: click_and_type("!gauntlet"))
button3 = tk.Button(root, text="!hitsquad", command=lambda: click_and_type("!hitsquad"))
button4 = tk.Button(root, text="!wizard", command=lambda: click_and_type("!wizard"))
button5 = tk.Button(root, text="!attack 1", command=lambda: click_and_type("!attack1"))
button6 = tk.Button(root, text="!attack 2", command=lambda: click_and_type("!attack2"))
button7 = tk.Button(root, text="!attack 3", command=lambda: click_and_type("!attack3"))
button8 = tk.Button(root, text="!attack 4", command=lambda: click_and_type("!attack4"))
button9 = tk.Button(root, text="!attack 5", command=lambda: click_and_type("!attack5"))
button10 = tk.Button(root, text="!flames", command=lambda: click_and_type("!flames"))
button11 = tk.Button(root, text="!moan", command=lambda: click_and_type("!moan"))
button12 = tk.Button(root, text="!shield", command=lambda: click_and_type("!shield"))

# Add the buttons to the GUI
button1.pack(fill=tk.BOTH, expand=True)
button2.pack(fill=tk.BOTH, expand=True)
button3.pack(fill=tk.BOTH, expand=True)
button4.pack(fill=tk.BOTH, expand=True)
button5.pack(fill=tk.BOTH, expand=True)
button6.pack(fill=tk.BOTH, expand=True)
button7.pack(fill=tk.BOTH, expand=True)
button8.pack(fill=tk.BOTH, expand=True)
button9.pack(fill=tk.BOTH, expand=True)
button10.pack(fill=tk.BOTH, expand=True)
button11.pack(fill=tk.BOTH, expand=True)
button12.pack(fill=tk.BOTH, expand=True)



# Start the GUI
root.mainloop()
