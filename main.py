# Import required modules
import tkinter as tk
import random

# Define globals
WIDTH = 1920
HEIGHT = 1080

# Define movingButton class
class movingButton:
    def __init__(self):
        global WIDTH, HEIGHT
        self.buttonObject = tk.Button(window, text="Click me", width = 25)
        self.buttonObject.bind("<Enter>", self.buttonDodge)
        self.xPosition = random.randint(0, WIDTH-30)
        self.yPosition = random.randint(0, HEIGHT-10)
        self.buttonObject.place(x=self.xPosition, y=self.yPosition)
        
    def buttonDodge(self, sth):
        initialX = self.xPosition
        initialY = self.yPosition
        while abs(initialX-self.xPosition) < 20:
            self.xPosition = random.randint(0, WIDTH-30)
        while abs(initialY-self.yPosition) < 20:
            self.yPosition = random.randint(0, HEIGHT-10)
        self.buttonObject.place(x=self.xPosition, y=self.yPosition)

    

# Create window object
window = tk.Tk()
window.geometry(str(WIDTH) + "x" + str(HEIGHT))
window.title("Program Backup Tool")

for x in range(100):
    movingButton()

window.mainloop()