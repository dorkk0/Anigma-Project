import sys
from Enigma import Enigma
import cProfile


# profiling to the while loop
profile = cProfile.Profile()
profile.enable()

while True:
    # enigma machine creation
    #('Z','U'), ('H','L'), ('C','Q'), ('W','M'), ('O','A'), ('P','Y'), ('E','B'), ('T','R'), ('D','N'), ('V','I')
    plugConfig = []
    enigma = Enigma(1, 2, 3,  # left rotor, middle rotor, right rotor
                    0, 0, 0,  # left setting,middle setting, right setting
                    5, 3, 21,  # left offset , middle offset,right offset
                    plugConfig)  # optional 10 pairs to plugboard

    # user interface handling
    print ('\n' * 3)
    message = "ENIGMA"

    #input("Enter a message to decipher (To Exit Enter-exit)\n"
    #                    "=================\n"
    #                  "Enter Message:")

    message = message.upper()
    if message == 'EXIT':  # char 1 for exit from the program
       break

    encryptedMessage = ''
    for letter in message:
        if letter == ' ':
            encryptedMessage += ' '
            continue
        encryptedMessage += enigma.encrypt(letter)
    print ("Encrypted Message:", encryptedMessage)
    print(enigma.lRotor.offset , enigma.mRotor.offset, enigma.rRotor.offset )


profile.disable()
print ('\n' * 10)
profile.print_stats(sort = 'time') # print the profile result
sys.exit(0)