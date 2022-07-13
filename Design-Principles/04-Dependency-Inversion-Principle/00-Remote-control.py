import enum


# Using enum class create enumerations
class State(enum.Enum):
   ON = 1
   OFF = 2


#Low level Component
class Television:

    def __init__(self):
        self.state = State.OFF

    def turnTVOff(self):
        print("Shutting Down TV")


    def turnTVOn(self):
        print("Switching On TV")

    def toggle(self):

        #if self.state == State.OFF
        if self.state.name == 'OFF':
            self.state = State.ON
            self.turnTVOn()
        else:
            self.state = State.OFF
            self.turnTVOff()


#High level Component
class RemoteControl():

    def __init__(self):
        self.tv = Television()

    def click(self):
        self.tv.toggle()


if __name__ == "__main__":

    tv = Television()
    remote = RemoteControl()

    #turn ON
    remote.click()

    #turn OFF
    remote.click()

    #turn ON
    remote.click()


