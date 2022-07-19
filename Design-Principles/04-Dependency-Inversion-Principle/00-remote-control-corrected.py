import sys
import enum


# Using enum class create enumerations
class State(enum.Enum):
   ON = 1
   OFF = 2

#High level Component
class AbstractRemoteControl:

    def __init__(self, className):
        self.controllers = className
        self.state = {className.__name__ : State.OFF}
        #print(self.state)

    def click(self):
        #return self.controllers.toggle(self.controllers)
        #if self.state == State.OFF
        if self.state[self.controllers.__name__].name == 'OFF':
            self.state[self.controllers.__name__] = State.ON
            self.controllers.turnOn(self.controllers)
        else:
            self.state[self.controllers.__name__] = State.OFF
            self.controllers.turnOff(self.controllers)


#Low level Component
class Television(AbstractRemoteControl):

    def turnOff(self):
        print("Shutting Down TV")

    def turnOn(self):
        print("Switching On TV")

class Sprinkler(AbstractRemoteControl):

    def turnOff(self):
        print("Shutting Sprinkler Off")

    def turnOn(self):
        print("Switching On Sprinkler")


def str_to_class(classname):
    #OR import the module and use in getattr
    return getattr(sys.modules[__name__], classname)

if __name__ == "__main__":


    
    remote = AbstractRemoteControl(str_to_class('Sprinkler'))
    #turn ON
    remote.click()

    remote = AbstractRemoteControl(str_to_class("Television"))
    #turn OFF
    remote.click()

    remote = AbstractRemoteControl(str_to_class('Sprinkler'))
    #turn ON
    remote.click()

    remote = AbstractRemoteControl(str_to_class("Television"))
    #turn OFF
    remote.click()

