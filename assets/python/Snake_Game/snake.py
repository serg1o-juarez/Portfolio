from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]
        #### This makes a triangle for the head segment
        self.head = self.segments[0]
        self.head.shape("triangle")
        self.head.color("green")
        self.head.shapesize(1,1)
        #### This makes the tail look like a rattlesnake's tail.
        #### removed because no matter what the tail grows and the circle get pushed in.
        # self.tail = self.segments[-1]
        # self.tail.shape("circle")
        # self.tail.color("cyan")
        # self.tail.shapesize(1,1)  

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segments(position)
   

    def add_segments(self, position):
        snake = Turtle("square")
        snake.color("lime")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        #### To set this up if we want 3,2,1 the start is 3 the stop is 1 and the step is -1 to count down from 3 to 1
        ### In this case since it's a list we want 2,1,0 so start is 2, stop is 0 and step is -1
        ### To do this for all upcoming segments we want the length of the segments -1 to start the stop is 0 and step is -1
                    ###len(self.segments)-1  = 2 because 0,1,2 in list   stop is 0 and counting down by -1
        for seg_num in range(len(self.segments)-1, 0, -1):
            ### This is where the second to last segments coordinates are set to variables for the last segment to move there.
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            ### the last segment is set to go to the second to last segments coordinates.
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
