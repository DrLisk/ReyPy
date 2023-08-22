import math
from tkinter import *

def splash(title, message, columns = 80):
    '''
    welcomeMessage(title, message, columns = 80)

    Prints a splash screen with a Title and Message string.
    Optional keyword arguments:
    columns: Int number of characters wide for the splash screen. Defaults to 80.
    '''
    bars = '-' * columns
    padding = math.floor((columns - len(message))/2)
    message = (' ' * padding) + message
    print(bars)
    print(Title)
    print(bars)
    print("")
    print("")
    print(message)
    print("")
    print("")


def openFile(title=None):
    '''
    openFile(title)

    Opens a file dialog box for a use to select a file.
    Returns the path to the file.
    '''
    return askopenfilename(title)
