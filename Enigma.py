from PlugBoard import PlugBoard
from Reflector import Reflector
from Rotor import Rotor
import sys

class Enigma():

    rotors = [Rotor(1, list("EKMFLGDQVZNTOWYHXUSPAIBRCJ"), "Q"), Rotor(2, list("AJDKSIRUXBLHWTMCQGZNPYFVOE"), "E")
              ,Rotor(3, list("BDFHJLCPRTXVZNYEIWGAKMUSQO"), "V"), Rotor(4, list("ESOVPZJAYQUIRHXLNFTGKDCMWB"), "J"),
              Rotor(5, list("VZBRGITYUPSDNHLXAWMJQOFECK"), "Z")]

    def __init__(self, lRotor , mRotor ,rRotor, lSettings, mSettings, rSettings, lOffset, mOffset, rOffset, config):

        self.setRotors(lRotor, mRotor , rRotor)

        self.setSettings(lSettings,mSettings,rSettings)

        self.setOffsets(lOffset, mOffset, rOffset)

        self.reflector = Reflector(list("YRUHQSLDPXNGOKMIEBFZCWVJAT"))

        self.plugboard = PlugBoard(config)




    def setRotors(self,l , m , r ):

        if r != m != l:
            self.rRotor = self.rotors[int(r) - 1]
            self.mRotor = self.rotors[int(m) - 1]
            self.lRotor = self.rotors[int(l) - 1]
        else:
            print("Must select 3 different rotors for the machin")
            sys.exit(0)


    def setSettings(self,l , m , r):

        if l.isalpha() and m.isalpha() and r.isalpha():
            if len(l) == 1 and len(m) == 1 and len(r) == 1:

                l = l.upper()
                m = m.upper()
                r = r.upper()

                self.rRotor.setSettings(ord(r)-ord('A'))
                self.mRotor.setSettings(ord(m)-ord('A'))
                self.lRotor.setSettings(ord(l)-ord('A'))
            else:
                print("Rotor's settings must be 1 letter only")
                sys.exit(0)

        else:
            print("Rotor's settings must be alphabetic")
            sys.exit(0)

    def setOffsets(self, l ,m,r ):

        if l.isalpha() and m.isalpha() and r.isalpha():
            if len(l) == 1 and len(m) == 1 and len(r) == 1:

                l = l.upper()
                m = m.upper()
                r = r.upper()

                self.rRotor.setOffset(ord(r) - ord('A'))
                self.mRotor.setOffset(ord(m) - ord('A'))
                self.lRotor.setOffset(ord(l) - ord('A'))
            else:
                print("Rotor's offset must be 1 letter only")
                sys.exit(0)
        else:
            print("Rotor's offset must be alphabetic")
            sys.exit(0)


    def encrypt(self, letter):
        #Check for turnover and doublestep
        if self.rRotor.turnOver() or self.mRotor.turnOver():
            if self.mRotor.turnOver():
                self.lRotor.step()

            self.mRotor.step()

        self.rRotor.step()

        #Encrypting the letter
        letter = self.plugboard.translation(letter)
        letter = self.rRotor.translation(letter)
        letter = self.mRotor.translation(letter)
        letter = self.lRotor.translation(letter)
        letter =  self.reflector.translation(letter)

        self.rRotor.changeDir()
        self.mRotor.changeDir()
        self.lRotor.changeDir()

        letter = self.lRotor.translation(letter)
        letter = self.mRotor.translation(letter)
        letter = self.rRotor.translation(letter)
        letter = self.plugboard.translation(letter)


        self.rRotor.changeDir()
        self.mRotor.changeDir()
        self.lRotor.changeDir()

        return letter




