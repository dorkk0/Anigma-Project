import sys
from Enigma import Enigma
import cProfile
import string
import random

# Assignment's input "UMDPQ CUAQN LVVSP IARKC TTRJQ KCFPT OKRGO ZXALD RLPUH AUZSO SZFSU GWFNF DZCUG VEXUU LQYXO TCYRP SYGGZ HQMAG PZDKC KGOJM MYYDD H"
# Assignment's plugboard config ('Z', 'U'), ('H', 'L'), ('C', 'Q'), ('W', 'M'), ('O', 'A'), ('P', 'Y'), ('E', 'B'), ('T', 'R'), ('D', 'N'), ('V', 'I')


#profiling to the while loop
profile = cProfile.Profile()
profile.enable()


#Enigma machine creation


plugConfig = []
machine_config = []


print('\n' * 4)

#Need to add -

#Ask input from user for the Enigma settings

message = input("Enter the rotors number you would like to use in the machine , left to right - ")
if message.isnumeric() == False:
    print("The rotors numbers must be numeric")
    sys.exit(0)


machine_config.append(list(message))



message = input("Enter the settings for each rotor right to left - ")

machine_config.append(list(message))


message = input("Enter the offsets for each rotor right to left - ")

machine_config.append(list(message))

message = input("Enter the plugboard's configuration , use space to separate each pair- ")
if len(message) != 0:
    plugConfig = message.upper()
    plugConfig = plugConfig.split(" ")
    plugConfig = list(map(tuple , plugConfig))



enigma = Enigma(machine_config[0][0], machine_config[0][1], machine_config[0][2],  # left rotor, middle rotor, right rotor
                machine_config[1][0], machine_config[1][1], machine_config[1][2],  # left setting,middle setting, right setting
                machine_config[2][0], machine_config[2][1], machine_config[2][2],  # left offset , middle offset,right offset
                plugConfig)  # optional 10 pairs to plugboard

while True:


    print ('\n' * 3)
    message = input("Enter a message in the machine (To Exit Enter-exit)\n"
                      "Enter Message:")

    message = message.upper()

    if message == 'EXIT':  # char 1 for exit from the program
       break

    encryptedMessage = ''
    for letter in message:
        if letter == ' ':
            encryptedMessage += ' '
            continue
        encryptedMessage += enigma.encrypt(letter)
    print ("Output:", encryptedMessage)



#Check performence of 10000 machines with random strings
# i=0
# while i!=10000:
#     r_message  = ''.join(random.choices(string.ascii_uppercase))
#     enigma.encrypt(r_message)
#     i+=1

profile.disable()
print ('\n' * 10)
profile.print_stats(sort = 'time') # print the profile result
sys.exit(0)