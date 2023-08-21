import math
def welcomeMessage(Title='Title', Message='Message', Columns = 80):
    bars = '-' * Columns
    padding = math.floor((Columns - len(Message))/2)
    Message = (' ' * padding) + Message
    print(bars)
    print(Title)
    print(bars)
    print("")
    print("")
    print(Message)
    print("")
    print("")
    


def readFile(FilePath=None):
    if FilePath==None: return
    return 0



