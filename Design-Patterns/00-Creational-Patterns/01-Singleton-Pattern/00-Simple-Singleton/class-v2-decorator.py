def singleton(class_):

    instance = {}

    print(class_)


    def get_instance(*args, **kwargs):

        if class_ not in instance:
            instance[class_] = class_(*args, **kwargs)
        return instance[class_]

    return get_instance



@singleton
class Database:
    def __init__(self):
        print('Loading Database')



if __name__ == "__main__":

    obj1 = Database()
    obj2 = Database()


    print(obj1 == obj2)

    obj3 = Database()
