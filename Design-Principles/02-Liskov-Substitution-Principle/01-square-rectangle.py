class Rectangle:
    
    def __init__(self, width, height):
        self._height = height
        self._width = width

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'

    @property
    def area(self):
        return self._width * self._height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):

    def __init__(self, size):
        super().__init__(size, size)

    @Rectangle.width.setter
    def width(self, value):

        if( (value != self._height)):
            raise Exception("Width and Height for Square cant be different")
        else:
            self._width = value
            self._height = value

    @Rectangle.height.setter
    def height(self, value):

        if((value != self._width) and (self._height != 0)) :
            raise Exception("Width and Height for Square cant be different")
        else:
            self._height = value
            self._width = value

def process(ob_list):

    for shapes in ob_list:
        print(shapes.area)




if __name__=="__main__":

    ob_list = [Rectangle(2, 3), Square(5), Square(7)]

    process(ob_list)