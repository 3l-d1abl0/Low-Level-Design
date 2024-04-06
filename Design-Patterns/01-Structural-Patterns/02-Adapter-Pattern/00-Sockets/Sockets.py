class EuropeanSocketInterface(object):

    def voltage(self):
        pass
    def live(self):
        pass
    def neutral(self):
        pass
    def earth(self):
        pass


class USASocketInterface(object):

    def voltage(self):
        pass
    def live(self):
        pass
    def neutral(self):
        pass


class EuropeanSocket(EuropeanSocketInterface):

    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1
