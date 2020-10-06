from names import names
from honorifics import honorifics
import random
import itertools


class Chooser(object):
    def __init__(self, names=names, honorifics=honorifics):
        self.names = names.copy()
        random.shuffle(self.names)
        self.name_next = itertools.cycle(self.names)
        self.honorifics = honorifics or ['ready']
        random.shuffle(self.honorifics)
        self.honorific_next = itertools.cycle(self.honorifics)
        
    def next(self):
        if not self.names or not honorifics:
            return ""
        return f"{next(self.name_next)}, {next(self.honorific_next)}"

if __name__ == "__main__":
    chooser = Chooser()
    while True:
        input("Press enter >")
        print(chooser.next())
