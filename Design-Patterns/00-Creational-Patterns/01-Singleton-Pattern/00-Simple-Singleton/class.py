class Singleton(object):
    __instance = None
    def __new__(cls, val):

        print(cls)
        if Singleton.__instance is None:
            Singleton.__instance = super(Singleton, cls).__new__(cls)
            #Singleton.__instance = object.__new__(cls)
            print('New: ', Singleton.__instance)
            Singleton.__instance.config = val
        else:
            print('Existing: ', Singleton.__instance)

        return Singleton.__instance

    #def __init__(self, val):self.config = val



if __name__ =="__main__":
    obj = Singleton('data1')
    print(obj.config)
    #print(dir(obj))

    obj = Singleton('data2')
    #print(dir(obj))
    print(obj.config)

    obj = Singleton('data3')
    print(obj.config)
    #print(dir(obj))
