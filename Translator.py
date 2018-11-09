#Class to change a letter to index and the othwer way around , includes using a curcular shift method

class Translator():

    def __init__(self):
        pass


    def indexToletter(self, index):
        return chr(index + ord('A'))


    def letterToindex(self,letter):
        return ord(letter) - ord('A')

    def circularshift(self, index, letter):
        if index < 0:
            index += 26

        return self.indexToletter(self.letterToindex(letter) + index) % 26





