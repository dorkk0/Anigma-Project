#Class to change a letter to index and the othwer way around , includes using a curcular shift method

class Translator():

    def __init__(self):
        pass


    def translation(selfs):
        pass

    def reversetranslation(self):
        base = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        i = 0
        for letter in self.permutation:
            self.reversepermutation[Translator.letterToindex(letter)] = base[i]
            i = i + 1


    @staticmethod
    def indexToletter(index):
        return chr(index + ord('A'))

    @staticmethod
    def letterToindex(letter):
        return ord(letter) - ord('A')

    def circularshift(self, index, letter):
        if index < 0:
            index += 26

        return self.indexToletter((self.letterToindex(letter) + index) % 26)





