import math

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
    
def readTXT(filepath):
    '''
    readTXT(filepath)

    Takes path to .txt file and returns a list of strings of each line of the file.
    Right hand side whitespace is removed.
    '''
    return [line.rstrip() for line in open(FilePath)]

def readCSV(filepath, newline=''):
    '''
    readCSV(filepath, newline='')

    Takes path to .csv file and returns a list of rows of the file.
    Optional keyword arguments:
    newline: new line delimeter for the file. Defaults to ''.
    '''
    with open(filepath, newline=newline) as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    return data
