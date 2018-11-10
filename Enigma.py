from PlugBoard import PlugBoard
from Reflector import Reflector
from Rotor import Rotor


class Enigma():

    rotors = [Rotor("I", list("EKMFLGDQVZNTOWYHXUSPAIBRCJ"), "Q"), Rotor("II", list("AJDKSIRUXBLHWTMCQGZNPYFVOE"), "E")
              ,Rotor("III", list("BDFHJLCPRTXVZNYEIWGAKMUSQO"), "V"), Rotor("IV", list("ESOVPZJAYQUIRHXLNFTGKDCMWB"), "J"),
              Rotor("V", list("VZBRGITYUPSDNHLXAWMJQOFECK"), "Z")]

    def __init__(self, rRotor, mRotor, lRotor, rSettings, mSettings, lSettings, rOffset, mOffset, lOffset, config):

        if rRotor != mRotor != lRotor:
            self.rRotor = self.rotors[rRotor - 1]
            self.mRotor = self.rotors[mRotor - 1]
            self.lRotor = self.rotors[lRotor - 1]

            self.rRotor.setSettings(rSettings)
            self.mRotor.setSettings(mSettings)
            self.lRotor.setSettings(lSettings)

            self.rRotor.setOffset(rOffset)
            self.mRotor.setOffset(mOffset)
            self.lRotor.setOffset(lOffset)

            self.reflector = Reflector(list("YRUHQSLDPXNGOKMIEBFZCWVJAT"))

            self.plugboard = PlugBoard(config)
        else:
            print("Must select 3 different rotors for the machin")


    def encrypt(self, letter):
        #Check for turnover and doublestep
        if self.rRotor.turnOver() or self.mRotor.turnOver():
            if self.mRotor.turnOver():
                self.lRotor.step()

            self.mRotor.step()

        self.rRotor.step()

        #Encrypting the letter
        letter = self.plugboard.translation(letter)
        print(letter)
        letter = self.rRotor.translation(letter)
        print(letter)
        letter = self.mRotor.translation(letter)
        print(letter)
        letter = self.lRotor.translation(letter)
        print(letter)
        letter =  self.reflector.translation(letter)
        print(letter)

        self.rRotor.changeDir()
        self.mRotor.changeDir()
        self.lRotor.changeDir()
        print("     ")
        letter = self.lRotor.translation(letter)
        print(letter)
        letter = self.mRotor.translation(letter)
        print(letter)
        letter = self.rRotor.translation(letter)
        print(letter)
        letter = self.plugboard.translation(letter)
        print(letter)

        self.rRotor.changeDir()
        self.mRotor.changeDir()
        self.lRotor.changeDir()

        return letter




