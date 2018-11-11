import sys
from Enigma import Enigma
import cProfile


# profiling to the while loop
profile = cProfile.Profile()
profile.enable()

while True:
    # enigma machine creation

    plugConfig = [('Z','U'), ('H','L'), ('C','Q'), ('W','M'), ('O','A'), ('P','Y'), ('E','B'), ('T','R'), ('D','N'), ('V','I')]
    enigma = Enigma(2, 5, 4,  # left rotor, middle rotor, right rotor
                    18, 8, 23,  # left setting,middle setting, right setting
                    ord('D') - ord('A'), ord('O') - ord('A'), ord('R') - ord('A'),  # left offset , middle offset,right offset
                    plugConfig)  # optional 10 pairs to plugboard

    # user interface handling
    print ('\n' * 3)
    message = "UMDPQ CUAQN LVVSP IARKC TTRJQ KCFPT OKRGO ZXALD RLPUH AUZSO SZFSU GWFNF DZCUG VEXUU LQYXO TCYRP SYGGZ HQMAG PZDKC KGOJM MYYDD H"

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
    break

profile.disable()
print ('\n' * 10)
profile.print_stats(sort = 'time') # print the profile result
sys.exit(0)