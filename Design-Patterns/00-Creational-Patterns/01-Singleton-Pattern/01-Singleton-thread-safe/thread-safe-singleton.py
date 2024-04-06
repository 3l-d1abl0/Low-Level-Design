from concurrent.futures import ThreadPoolExecutor
import threading
from concurrent.futures import as_completed


class Singleton(object):
    __instance = {}
    __singleton_lock = threading.Lock()

    def __new__(cls, *args, **kwargs): #gets called __init__

        '''
        with cls.__singleton_lock:
            if cls not in cls.__instance:
                cls.__instance[cls] = super(Singleton, cls).__new__(cls)
                cls.__instance[cls].config = args[0]



        '''
        cls.__singleton_lock.acquire()
        try:
            if cls not in cls.__instance:
                cls.__instance[cls] = super(Singleton, cls).__new__(cls)
                cls.__instance[cls].config = args[0]
        finally:
            cls.__singleton_lock.release()

        #

        return cls.__instance[cls]



def create_object(config):
        obj1 = Singleton(config)
        print(obj1.config)
        #print(dir(obj))

        obj2 = Singleton(config)
        #print(dir(obj))
        print(obj2.config)

        obj3 = Singleton(config)
        print(obj3.config)

        obj4 = Singleton(config)
        print(obj4.config)


        print(obj1==obj2)
        print(obj2==obj3)
        print(obj3==obj4)
        return 'Function !'

if __name__ =="__main__":

    with ThreadPoolExecutor(max_workers=7) as executor:

        futures = [executor.submit(create_object, 'Config_'+str(idx)) for idx in range(10)]
        for future in as_completed(futures):
            print('->', future.result())

    print('Done')
