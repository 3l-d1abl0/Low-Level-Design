from Sockets import USASocketInterface

class Adapter(USASocketInterface):

    __socket = None



    def __init__(self, socket):
        self.__socket = socket


    def voltage(self):
        return 110

    def live(self):
        return self.__socket.live()

    def neutral(self):
        return self.__socket.neutral()
