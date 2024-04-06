class Singleton(object):
    __instance = {}

    def __new__(cls, *args, **kwargs): #gets called before __init__

        print(cls)
        if cls not in cls.__instance:
            instance = object.__new__(cls)
            cls.__instance[cls] = super(Singleton, cls).__new__(cls)
            cls.__instance[cls].config = args[0]

        return cls.__instance[cls]



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
