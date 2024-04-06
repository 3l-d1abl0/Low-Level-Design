from factory import ShapeFactory, ShapeSystem
import random

if __name__ == "__main__":

    shape_factory = ShapeFactory()
    shapes = []

    shape_type = random.choice([ShapeSystem.CIRCLE, ShapeSystem.RECTANGLE])
    shapes.append(shape_factory.create_shape(shape_type, 0,1))


    shape_type = random.choice([ShapeSystem.CIRCLE, ShapeSystem.RECTANGLE])
    shapes.append(shape_factory.create_shape(shape_type, 10,21))

    shape_type = random.choice([ShapeSystem.CIRCLE, ShapeSystem.RECTANGLE])
    shapes.append(shape_factory.create_shape(shape_type, 50,81))


    #Draw the shapes
    for shape in shapes:
        shape.draw("Canvas")
