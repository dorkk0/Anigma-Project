import sys

from Translator import Translator


class PlugBoard(Translator):

    def __init__(self, config):
        self.permutation = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.setConfig(config)


    def setConfig(self, config):

        if len(config) > 10:
            print("Error, number of pairs in configuration must be at most 10 paris")
            sys.exit(0)

        elif len(config) > 0 and len(config) <= 10:
           for pair in config:
               f_letter = pair[0]
               s_letter = pair[1]
               f_index = self.letterToindex(f_letter)
               s_index = self.letterToindex(s_letter)
               self.permutation[f_index] = s_letter
               self.permutation[s_index] = f_letter

    def translation(self, letter):
        return self.permutation[self.letterToIndex(letter)]



























