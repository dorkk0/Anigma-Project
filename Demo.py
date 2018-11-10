import sys
from Enigma import Enigma
import cProfile


# profiling to the while loop
profile = cProfile.Profile()
profile.enable()

while True:
    # enigma machine creation

    plugConfig = [('Z','U'), ('H','L'), ('C','Q'), ('W','M'), ('O','A'), ('P','Y'), ('E','B'), ('T','R'), ('D','N'), ('V','I')]
    enigma = Enigma(4, 5, 2,  # right rotor, middle rotor, left rotor
                    24, 9, 19,  # right setting,middle setting, left setting
                    14, 15, 3,  # right offset , middle offset,left offset
                    plugConfig)  # optional 10 pairs to plugboard

    # user interface handling
    print ('\n' * 3)
    message = input("Enigma M3 Machine (To Exit Enter-1)\n"
                        "=================\n"
                        "Enter Message:")
    if message == '1':  # char 1 for exit from the program
        break

    encryptedMessage = ''
    for letter in message:
        if letter == ' ':
            encryptedMessage += ' '
            continue
        encryptedMessage += enigma.encrypt(letter)
    print ("Encrypted Message:", encryptedMessage)

profile.disable()
print ('\n' * 10)
profile.print_stats(sort = 'time') # print the profile result
sys.exit(0)