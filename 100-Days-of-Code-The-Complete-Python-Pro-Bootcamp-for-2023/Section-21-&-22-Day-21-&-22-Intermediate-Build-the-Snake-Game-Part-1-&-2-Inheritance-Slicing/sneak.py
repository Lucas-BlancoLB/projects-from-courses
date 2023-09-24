from turtle import Screen, Turtle, reset
from time import sleep

# for each key there's two terms, the angle-coordinates are in order [left, right] → logical in Sneak.move()
DIRECTIONS = {
    "w": [0, 180],
    "s": [180, 0],
    "a": [90, 270],
    "d": [270, 90]
}

SPEED = 0.05  # Default 0.1


class Sneak:
    # __init__ method = the creator method
    def __init__(self):
        self.screen = Screen()
        self.segments = []
        self.is_moving = False
        self.create_segments(30)
        self.head = self.segments[0]
        self.DIRECTIONS = DIRECTIONS
        self.screen.update()

    def create_segments(self, n_segments):
        """Create a sneak using segments | first segment will be the head"""
        x = 0
        for i in range(n_segments):
            square = Turtle(shape='square')
            square.speed(0)
            square.penup()
            square.color('black')

            square.setx(x)

            x -= 20
            self.segments.append(square)
            # square.screen.update()
            # print(self.segments)

    def add_segment(self):
        self.create_segments(1)

    ''' MOTION '''

    def move(self, direction):
        """"movement method, it uses Screen.onkeypress(fun=lambda: , key="") inputted as direction"""
        if direction in self.DIRECTIONS:

            # it recognises if the key pressed by the current angle-position should turn left or right
            if self.DIRECTIONS[direction][0] == self.head.heading():
                self.turn_counter_clockwise()
            elif self.DIRECTIONS[direction][1] == self.head.heading():
                self.turn_clockwise()

    def move_forward(self):
        """to make the snake move forward"""
        self.is_moving = True
        while self.is_moving:
            self.screen.update()
            sleep(SPEED)
            for fd in range(len(self.segments) - 1, 0, -1):
                self.segments[fd].setposition(self.segments[fd - 1].position())
            self.head.forward(20)

    def turn_clockwise(self):
        """'To make the sneak turn right"""
        for r in range(len(self.segments) - 1, 0, -1):
            self.segments[r].setposition(self.segments[r - 1].position())
        self.head.setheading(self.head.heading() - 90)
        self.head.forward(20)
        self.screen.update()

    def turn_counter_clockwise(self):
        """'To make the sneak turn left"""
        for l in reversed(range(1, len(self.segments))):
            self.segments[l].setposition(self.segments[l - 1].position())
        self.head.setheading(self.head.heading() + 90)
        self.head.forward(20)
        self.screen.update()

    def restart(self):  # HERE
        for i in range(len(self.segments) - 1, -1 , -1):
            self.segments[i].hideturtle()

        self.__init__()