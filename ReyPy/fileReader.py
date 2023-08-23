    
'''
TODO:
    Add support for .xls files
    File writing?
    Branch out file name to include writing? Or seperate file?
'''
def TXT(filepath):
    '''
    TXT(filepath)

    Takes path to .txt file and returns a list of strings of each line of the file.
    Right hand side whitespace is removed.
    '''
    return [line.rstrip() for line in open(filePath)]

def CSV(filepath, newline=''):
    '''
    CSV(filepath, newline='')

    Takes path to .csv file and returns a list of rows of the file.
    Optional keyword arguments:
    newline: new line delimeter for the file. Defaults to ''.
    '''
    with open(filepath, newline=newline) as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    return data

def GERBER(filepath):
    '''
    GERBER(filepath)

    Takes the path to a gerber file and returns a list of strings containing the commands.
    '''
    return [line.rstrip() for line in open(filePath)]
