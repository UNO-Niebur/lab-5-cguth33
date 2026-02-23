#LetterFrequency.py
#Name:Carter Guthrie
#Date:2/22/26
#Assignment:Lab 5

#This program will create a CSV file of frequencies based on a text file.
#Use Excel or similar spreadsheet software to visualize the frequencies of the CSV file.

import os

def countLetters(message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()
    freq = [0] * 26 # Initialize list with 26 zeros

    # Loop through the message and count
    for letter in message:
        if letter in alpha:
            index = alpha.find(letter)
            freq[index] += 1

    # Format the data for CSV
    output = ""
    for i in range(26):
        line = alpha[i] + "," + str(freq[i]) + "\n"
        output += line
    
    writeToFile(output)

def writeToFile(fileText):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)
    freqFile = open("frq.csv", 'w')
    freqFile.write(fileText)
    freqFile.close()

def main():
    msg = input("Enter a message: ")
    countLetters(msg)
    print("Frequency data saved to frq.csv")

if __name__ == '__main__':
    main()