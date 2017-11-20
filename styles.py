from singleton import Singleton


class Styles(Singleton):

    def eyebrows(self):
        return self.eyebrows

    def eyeliner(self):
        return self.eyeliner

    def lips(self):
        return self.lips

    def set_eyebrows(self, eyebrows):
        self.eyebrows = eyebrows

    def set_eyeliner(self, eyeliner):
        self.eyeliner = eyeliner

    def set_lips(self, lips):
        self.lips = lips
