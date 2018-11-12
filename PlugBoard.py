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
           #checks if there are only 2 letters in each switch
           for pair in config:
               if len(pair)!=2:
                   print("plugboard configuration isn't legal")
                   sys.exit(0)
           #checks if each letter appear only once in the configuration
           for pair in config:
               for pair2 in config:
                   if pair != pair2:
                       if pair2.count(pair[0]) !=0 or pair2.count(pair[1]) !=0:
                           print("illegal plugboard configuration, each pair of letters must contain different letters")
                           sys.exit(0)
           for pair in config:
               f_letter = pair[0]
               s_letter = pair[1]
               f_index = Translator.letterToindex(f_letter)
               s_index = Translator.letterToindex(s_letter)
               self.permutation[f_index] = s_letter
               self.permutation[s_index] = f_letter

    def translation(self, letter):
        return self.permutation[Translator.letterToindex(letter)]



























