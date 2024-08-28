import time
import pyautogui as p
import tkinter as tk
def screenshot():
    name = int(round(time.time() * 1000))  # Generate a unique name based on current time
    name = '{}.png'.format(name)  # Format the name as a PNG file
    time.sleep(5)  # Wait for 5 seconds
    img = p.screenshot(name)  # Take a screenshot and save it with the generated name
    img.show()  # Display the taken screenshot

#screenshot()  # Call the screenshot function

root=tk.Tk()
frame=tk.Frame(root)
frame.pack()

button=tk.Button(
    frame,
    text='Take ScreenShott',
    command=screenshot)

button.pack(side=tk.LEFT)
close=tk.Button(
    frame,
    text='Exitt',
    command=quit
)
close.pack(side=tk.LEFT)
root.mainloop()