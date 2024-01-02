from turtle import Turtle, register_shape

import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


class CarManager:

    def __init__(self):
        self.is_game_on = True
        self.images = ["car1.gif", "car2.gif", "car3.gif", "car4.gif", "car5.gif"]
        for shape in self.images:
            register_shape(shape)
        self.spawn_car = 9
        self.Y_COR = [-230, -170, -110, -50, 10, 70, 130, 190, 250]
        self.index = int()
        self.cars = []
        self.creating_cars()
        self.move_increment = 10


    def creating_cars(self):
        X_COR = 360

        for index in range(self.spawn_car):
            # while self.is_game_on:
            car = Turtle()
            car.shape(random.choice(self.images))
            car.penup()

            if self.spawn_car != 1:
                car.setposition(X_COR, self.Y_COR[index])
                X_COR += 30



            else:
                # print(round(self.index))
                car.setposition(360, self.Y_COR[self.index])
            car.setheading(180)
            # print(car.shapesize())
            self.cars.append(car)


    def reset_cars(self):
        for var in self.cars:
            var.setx(-360)
            var.hideturtle()
        self.__init__()

    def if_car_touches_border(self):
        for is_at_border in self.cars:
            if is_at_border.xcor() <= -360:
                self.index = int(self.Y_COR.index(round(is_at_border.ycor())))
                self.spawn_car = 1
                self.cars.remove(is_at_border)
                is_at_border.hideturtle()
                self.creating_cars()


    def cars_moving(self):
        var = random.choice(self.cars)
        var.forward(self.move_increment)

