"""
Name:       Joseph Maiello
Date:       11/18/2021   
Program:    ComissionCalc.py 

*** Note: the file breezypythongui.py MUST be in the same directory as this file for the application to work.
ALSO NOTE: Please install the package PIL with the command: pip install pillow before using this with a non GIF image.
***
"""
import math
from breezypythongui import EasyFrame
from tkinter.font import Font
class ComissionCalc(EasyFrame):
    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = "Lorem Ipsum Commission Calculator", background = "RoyalBlue3", resizable = False)
        # Title label
        titleFont = Font(family = "Arial", size = 20)
        self.titleLabel = self.addLabel(text = "Commission Calculator", row = 0, column = 0, columnspan = 4, background = "Lavender blush", sticky = "NEWS", font = titleFont)
        # Label and fields for the price of the house and commision rate
        self.addLabel(text = "Please enter the price of the property:", row = 1, column = 1, sticky = "NEWS")
        self.propertyField = self.addIntegerField(value = 0, row = 1, column = 2)
        self.addLabel(text = "Please enter your Commission rate:", row = 2, column = 1, sticky = "NEWS")
        self.commissionField = self.addIntegerField(value = 0, row = 2, column = 2, sticky = "NEWS")
        # Command button
        self.calcBtn = self.addButton(text = "Calculate", row = 3, column = 0, command = self.calc)
        self.resetBtn =self.addButton(text = "Reset", row = 3, column = 3, command = self.reset)
        # calculate the total ammount of commision earned
        self.outputField = self.addIntegerField(value = "You're total amount earned will be displayed here", row = 3, column = 1, columnspan = 2, sticky = "NEWS")
    # Event handling Method
    def calc(self):
        # Take the user input and multiply that number by the commision rate and display the result" 
        propTotal = self.propertyField.getNumber()
        commTotal = self.commissionField.getNumber() * 0.01
        totalEarned = propTotal * commTotal
        self.outputField.setNumber(totalEarned)
        self.calcBtn["state"] = "disabled"
        self.resetBtn["state"] = "normal"
        # Call to the resetBtn to clear out previous input and return to its original state
    def reset(self):
        self.propertyField.setNumber(0)
        self.commissionField.setNumber(0)
        self.outputField.setValue("You're total amount earned will be displayed here")
        self.calcBtn["state"] = "normal"
        self.resetBtn["state"] = "disabled"

# definition of the main() function for the program entry
def main():
    """Instantiates and pops up the winow."""
    ComissionCalc().mainloop()

# global call to trigger the main() function
if __name__ == "__main__":  
    main()
