<<<<<<< HEAD
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



=======
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def readFile(FilePath=None):
    if FilePath=None: return
    return 0
>>>>>>> 02124660032b1018dc8a0ff0a1d8e676838ddb56
