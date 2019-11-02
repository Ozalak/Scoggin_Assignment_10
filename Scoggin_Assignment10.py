import os

filePath = input('Enter directory to save the file in: ')#'C:/Users/Tibilan/Documents/Python_class'
if os.path.isdir(filePath): #check if file path exists
    fileName = input('Enter the file name: ')#'TestFile.txt'
    with open(fileName, 'w+') as fileHandle:
        fileHandle.write(input('Enter your name: ') + ', '
         + input("Enter your address: ") + ', ' + input('Enter your phone number: '))
    with open(fileName, 'r') as fileHandle:
        data = fileHandle.read()
    print('Validating Input:')
    print(data)
