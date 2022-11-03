# Import required modules
import tkinter as tk
import random

# Define globals
WIDTH = 1000
HEIGHT = 500
cellDivision = False
buttonNumber = 0

# Define movingButton class
class movingButton:
    def __init__(self):
        global WIDTH, HEIGHT
        self.buttonObject = tk.Button(window, text="Click me", width = 25)
        self.buttonObject.bind("<Enter>", self.buttonDodge)
        self.xPosition = random.randint(0, WIDTH-50)
        self.yPosition = random.randint(0, HEIGHT-20)
        self.buttonObject.place(x=self.xPosition, y=self.yPosition)
        
    def buttonDodge(self, sth):
        global cellDivision
        initialX = self.xPosition
        initialY = self.yPosition
        while abs(initialX-self.xPosition) < 20:
            self.xPosition = random.randint(0, WIDTH-50)
        while abs(initialY-self.yPosition) < 20:
            self.yPosition = random.randint(0, HEIGHT-20)
        self.buttonObject.place(x=self.xPosition, y=self.yPosition)
        if cellDivision == True:
            movingButton()
            
# Define xubmit button function
def submitFunction():
    global buttonNumber, numberInput, setupWindow
    buttonNumber = int(numberInput.get())
    setupWindow.destroy()

def updateCellDivision():
    global cellDivision, checkBox
    cellDivision = checkVar.get()

# Create setup window object
setupWindow = tk.Tk()
setupWindow.geometry("300x100")

# Create text
text = tk.Label(setupWindow, text="Number of buttons:")
text.place(x=0, y=0)
# Create text entry object
numberInput = tk.Entry(setupWindow)
numberInput.place(x=110, y=0)

# Create submit button object
submitButton = tk.Button(setupWindow, command=submitFunction, text="Submit", width = 25)
submitButton.place(x=0, y=45)

# Create check box object
checkVar = tk.BooleanVar()
checkBox = tk.Checkbutton(setupWindow, text="Cell division?", variable=checkVar, onvalue=True, offvalue=False, command = updateCellDivision)
checkBox.place(x=0, y=20)
# Setup window run
setupWindow.mainloop()



# Create window object
window = tk.Tk()
window.geometry(str(WIDTH) + "x" + str(HEIGHT))

for x in range(buttonNumber):
    movingButton()

window.mainloop()