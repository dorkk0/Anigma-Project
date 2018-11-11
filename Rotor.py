from Translator import Translator


class Rotor(Translator):
    alphabet_size = 26
    dir = "FW"
    def __init__(self, num, permutation, turnOverN):
        self.num=num
        self.permutation = permutation
        self.turnOverN = Translator.letterToindex(turnOverN)
        self.offset = 0
        self.settings = 0
        self.reversepermutation = [0]*self.alphabet_size
        self.reversetranslation()

    def getSettings(self):
        return self.settings


    def setSettings(self,settings):
        self.settings = settings

    def setOffset(self, offset):
        self.offset= offset


    def step(self):
        if self.offset == self.alphabet_size:
            self.offset = 0

        self.offset = self.offset + 1

    def turnOver(self):
        if self.offset != self.turnOverN:
            return False
        return True


    def changeDir(self):
        if self.dir == "FW":
            self.dir = "REV"
        else:
            self.dir = "FW"

    def translation(self,letter):
        message = self.circularshift(self.offset-self.settings,letter)

        if self.dir == "FW":
            newmessage = self.permutation[Translator.letterToindex(message)]

        else:
            newmessage = self.reversepermutation[Translator.letterToindex(message)]

        return self.circularshift((self.settings - 1) - (self.offset -1) , newmessage)











