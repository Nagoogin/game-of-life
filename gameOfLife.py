# Game of Life

import turtle
import random
import sys

SIZE = 5

class Grid:

    def __init__(self, xspan, yspan):
        self.state = set()
        self.xspan, self.yspan = xspan, yspan

    def set(self, x, y):
        key = (x, y)
        self.state.add(key)

    def flip_state(self, x, y):
        # if the cell is alive -> dead
        # if the cell is dead -> alive
        key = (x, y)
        if key in self.state:
            self.state.remove(key)
        else:
            self.state.add(key)

    def clear_board(self):
        self.state.clear()

    def step(self):
        post_step_state = set()
        for i in range(self.xspan):
            # creates a range of the x-adjacent cells
            x_range = range(i-1, i+2)
            for j in range(self.yspan):
                s = 0
                live = ((i, j) in self.state)
                # creates a range of the y-adjacent cells
                for y_pos in range(j-1, j+2):
                    for x_pos in x_range:
                        if (x_pos, y_pos) in self.state:
                            s += 1
                # removes the cell in question from the count of adjacent cells
                # subtracts either a 1 or 0 depending on the state of the cell
                s -= live
                if s == 3:
                    # A cell is born
                    post_step_state.add((i, j))
                elif s == 2 and live:
                    # The cell remains alive
                    post_step_state.add((i, j))
                    # All other cases result in death

        self.state = post_step_state

    def draw(self, x, y):
        turtle.penup()
        key = (x, y)
        if key in self.state:
            turtle.setpos(x*SIZE, y*SIZE)
            turtle.color('red')
            # perhaps make new cells 'green' for their first generation
            turtle.pendown()
            # sets the direction of the turtle 0 degrees (->)
            turtle.setheading(0)
            turtle.begin_fill()
            # traces out the square in a counter clockwise path
            for i in range(4):
                turtle.forward(SIZE-1)
                turtle.left(90)
            turtle.end_fill()

    def display(self):
        turtle.clear()
        # draws all live cells from grid.state
        for i in range(self.xspan):
            for j in range(self.yspan):
                self.draw(i, j)
        turtle.update()

    # prints out the keys of the live cells
    def print_keys(self):
        for key in self.state:
            print(key)

    # inputs the coordinates for a Glider at the top left corner of the grid
    def glider(self):
        points = [(3.0, 56.0), (2.0, 56.0), (1.0, 56.0), (3.0, 57.0), (2.0, 58.0)]
        for key in points:
            self.state.add(key)

    # inputs the coordinates for a Garden of Eden on the grid
    def garden(self):
        points = [(24.0, 30.0),(52.0, 35.0),(25.0, 31.0),(53.0, 34.0),(26.0, 28.0),
                  (33.0, 36.0),(47.0, 28.0),(52.0, 28.0),(41.0, 36.0),(32.0, 31.0),
                  (36.0, 34.0),(42.0, 35.0),(54.0, 30.0),(34.0, 29.0),(39.0, 32.0),
                  (26.0, 32.0),(49.0, 32.0),(28.0, 35.0),(23.0, 35.0),(41.0, 29.0),
                  (22.0, 28.0),(31.0, 35.0),(35.0, 36.0),(34.0, 36.0),(27.0, 28.0),
                  (32.0, 28.0),(28.0, 31.0),(43.0, 36.0),(42.0, 36.0),(49.0, 28.0),
                  (34.0, 30.0),(30.0, 29.0),(35.0, 31.0),(51.0, 34.0),(40.0, 29.0),
                  (32.0, 35.0),(37.0, 29.0),(42.0, 31.0),(40.0, 35.0),(35.0, 35.0),
                  (43.0, 30.0),(23.0, 28.0),(41.0, 34.0),(48.0, 30.0),(36.0, 36.0),
                  (28.0, 28.0),(24.0, 36.0),(38.0, 35.0),(45.0, 28.0),(44.0, 36.0),
                  (50.0, 28.0),(25.0, 33.0),(30.0, 30.0),(27.0, 34.0),(51.0, 33.0),
                  (22.0, 32.0),(31.0, 31.0),(46.0, 29.0),(36.0, 29.0),(30.0, 32.0),
                  (40.0, 32.0),(38.0, 31.0),(44.0, 30.0),(24.0, 33.0),(49.0, 36.0),
                  (24.0, 31.0),(50.0, 35.0),(47.0, 34.0),(46.0, 30.0),(53.0, 33.0),
                  (26.0, 29.0),(52.0, 29.0),(34.0, 32.0),(36.0, 35.0),(33.0, 29.0),
                  (39.0, 29.0),(54.0, 31.0),(37.0, 34.0),(41.0, 31.0),(44.0, 35.0),
                  (45.0, 34.0),(26.0, 33.0),(24.0, 28.0),(46.0, 36.0),(52.0, 33.0),
                  (50.0, 36.0),(41.0, 28.0),(47.0, 33.0),(54.0, 36.0),(53.0, 36.0),
                  (26.0, 30.0),(29.0, 33.0),(22.0, 29.0),(31.0, 34.0),(27.0, 31.0),
                  (32.0, 29.0),(29.0, 29.0),(48.0, 35.0),(35.0, 30.0),(26.0, 34.0),
                  (49.0, 34.0),(22.0, 36.0),(40.0, 30.0),(46.0, 33.0),(28.0, 33.0),
                  (32.0, 36.0),(47.0, 36.0),(30.0, 36.0),(37.0, 28.0),(54.0, 33.0),
                  (29.0, 36.0),(42.0, 28.0),(23.0, 33.0),(40.0, 36.0),(33.0, 33.0),
                  (35.0, 34.0),(23.0, 31.0),(41.0, 33.0),(48.0, 31.0),(28.0, 29.0),
                  (43.0, 34.0),(49.0, 30.0),(50.0, 29.0),(51.0, 32.0),(22.0, 33.0),
                  (31.0, 30.0),(36.0, 30.0),(51.0, 30.0),(23.0, 36.0),(32.0, 33.0),
                  (30.0, 33.0),(37.0, 31.0),(31.0, 36.0),(38.0, 28.0),(53.0, 28.0),
                  (43.0, 28.0),(48.0, 28.0),(44.0, 31.0),(43.0, 33.0),(24.0, 34.0),
                  (45.0, 30.0),(25.0, 35.0),(50.0, 30.0),(27.0, 32.0),(25.0, 29.0),
                  (22.0, 34.0),(46.0, 31.0),(53.0, 32.0),(47.0, 30.0),(30.0, 34.0),
                  (52.0, 30.0),(34.0, 33.0),(33.0, 28.0),(42.0, 33.0),(39.0, 28.0),
                  (54.0, 28.0),(37.0, 33.0),(44.0, 28.0),(39.0, 34.0),(45.0, 33.0),
                  (47.0, 32.0),(29.0, 32.0),(27.0, 30.0),(34.0, 34.0),(32.0, 30.0),
                  (36.0, 33.0),(33.0, 31.0),(38.0, 36.0),(37.0, 36.0),(29.0, 28.0),
                  (44.0, 33.0),(34.0, 28.0),(25.0, 36.0),(48.0, 36.0),(39.0, 33.0),
                  (45.0, 36.0),(51.0, 36.0),(49.0, 33.0),(28.0, 34.0),(29.0, 35.0),
                  (33.0, 32.0),(42.0, 29.0),(22.0, 31.0),(31.0, 32.0),(23.0, 30.0),
                  (41.0, 32.0),(28.0, 30.0),(38.0, 33.0),(29.0, 31.0),(39.0, 36.0),
                  (30.0, 28.0),(48.0, 33.0),(27.0, 36.0),(26.0, 36.0),(35.0, 28.0),
                  (40.0, 28.0),(46.0, 35.0),(36.0, 31.0),(52.0, 36.0),(32.0, 34.0),
                  (54.0, 35.0),(33.0, 35.0),(42.0, 30.0),(40.0, 34.0),(35.0, 32.0),
                  (23.0, 29.0),(48.0, 29.0),(43.0, 32.0),(50.0, 31.0),(27.0, 35.0),
                  (25.0, 28.0),(50.0, 33.0),(22.0, 35.0),(31.0, 28.0),(46.0, 28.0),
                  (28.0, 36.0),(36.0, 28.0),(51.0, 28.0),(52.0, 31.0),(38.0, 30.0),
                  (53.0, 30.0),(39.0, 31.0),(54.0, 29.0),(37.0, 32.0),(44.0, 29.0),
                  (24.0, 32.0),(45.0, 32.0)]
        for key in points:
            self.state.add(key)

    # inputs the coordinates for a Gosper Glider Gun on the grid
    def glider_gun(self):
        points = [(23.0, 51.0),(25.0, 51.0),(17.0, 51.0),(21.0, 53.0),(1.0, 51.0),
                  (36.0, 53.0),(13.0, 48.0),(11.0, 50.0),(22.0, 53.0),(12.0, 53.0),
                  (17.0, 52.0),(18.0, 51.0),(15.0, 51.0),(1.0, 52.0),(25.0, 55.0),
                  (16.0, 49.0),(2.0, 51.0),(22.0, 54.0),(21.0, 54.0),(23.0, 55.0),
                  (11.0, 52.0),(13.0, 54.0),(35.0, 54.0),(25.0, 50.0),(2.0, 52.0),
                  (11.0, 51.0),(17.0, 50.0),(22.0, 52.0),(21.0, 52.0),(14.0, 48.0),
                  (25.0, 56.0),(35.0, 53.0),(12.0, 49.0),(36.0, 54.0),(16.0, 53.0),
                  (14.0, 54.0)]
        for key in points:
            self.state.add(key)

    # inputs the coordinates for a Sparky
    def sparky(self):
        points = [(63.0, 28.0),(78.0, 28.0),(73.0, 32.0),(48.0, 31.0),(67.0, 33.0),
                  (51.0, 27.0),(50.0, 29.0),(48.0, 32.0),(52.0, 28.0),(71.0, 31.0),
                  (58.0, 36.0),(74.0, 32.0),(69.0, 28.0),(74.0, 28.0),(56.0, 30.0),
                  (59.0, 26.0),(54.0, 34.0),(77.0, 34.0),(72.0, 34.0),(57.0, 31.0),
                  (60.0, 29.0),(53.0, 28.0),(58.0, 28.0),(74.0, 25.0),(66.0, 33.0),
                  (52.0, 32.0),(48.0, 28.0),(62.0, 31.0),(78.0, 32.0),(64.0, 31.0),
                  (55.0, 26.0),(70.0, 27.0),(69.0, 33.0),(72.0, 27.0),(75.0, 25.0),
                  (60.0, 26.0),(57.0, 34.0),(58.0, 25.0),(73.0, 26.0),(53.0, 32.0),
                  (51.0, 29.0),(54.0, 27.0),(70.0, 28.0),(56.0, 27.0),(50.0, 27.0),
                  (57.0, 26.0),(60.0, 33.0),(56.0, 32.0),(59.0, 28.0),(64.0, 28.0),
                  (57.0, 29.0),(60.0, 31.0),(64.0, 32.0),(63.0, 29.0),(71.0, 33.0),
                  (62.0, 29.0),(72.0, 29.0),(51.0, 33.0),(66.0, 27.0),(74.0, 35.0),
                  (51.0, 31.0),(62.0, 33.0),(56.0, 29.0),(75.0, 30.0),(72.0, 33.0),
                  (71.0, 27.0),(70.0, 33.0),(58.0, 32.0),(58.0, 31.0),(48.0, 27.0),
                  (61.0, 34.0),(59.0, 30.0),(72.0, 26.0),(63.0, 31.0),(59.0, 32.0),
                  (58.0, 24.0),(67.0, 32.0),(53.0, 33.0),(54.0, 26.0),(72.0, 31.0),
                  (75.0, 29.0),(55.0, 34.0),(48.0, 33.0),(57.0, 27.0),(69.0, 27.0),
                  (56.0, 31.0),(62.0, 27.0),(57.0, 30.0),(78.0, 30.0),(73.0, 34.0),
                  (53.0, 27.0),(58.0, 29.0),(77.0, 26.0),(75.0, 35.0),(48.0, 29.0),
                  (62.0, 28.0),(67.0, 28.0),(57.0, 33.0),(69.0, 32.0),(60.0, 27.0),
                  (50.0, 31.0),(59.0, 34.0),(71.0, 29.0),(61.0, 26.0),(50.0, 33.0),
                  (62.0, 32.0),(56.0, 28.0),(75.0, 31.0),(64.0, 29.0),(70.0, 32.0),
                  (73.0, 28.0),(58.0, 35.0),(60.0, 34.0),(56.0, 33.0),(54.0, 33.0),
                  (63.0, 32.0),(67.0, 27.0)]
        for key in points:
            self.state.add(key)

def main():
    screen = turtle.Screen()
    turtle.mode('standard')
    xspan, yspan = screen.screensize()
    turtle.setworldcoordinates(0, 0, xspan, yspan)

    # makes the turtle invisible, improves drawing speed
    turtle.hideturtle()
    # fastest speed for the drawing
    turtle.speed('fastest')
    # no tracing within turtle, improves drawing speed
    turtle.tracer(0, 0)
    # turtle pen is off the canvas to start
    turtle.penup()

    board = Grid(xspan // SIZE, yspan // SIZE)

    def flip_state(x, y):
        x_cell = x // SIZE
        y_cell = y // SIZE
        board.flip_state(x_cell,y_cell)
        board.display()

    turtle.onscreenclick(turtle.listen)
    turtle.onscreenclick(flip_state)

    def clear_board():
        board.clear_board()
        board.display()
    # binds function to the 'e' key
    turtle.onkey(clear_board, 'e')

    # binds function to the 'q' key
    turtle.onkey(sys.exit, 'q')

    continuous = False
    def step_once():
        # allows for the rebinding of variables outside of the local scope
        nonlocal continuous
        continuous = False
        perform_step()

    def step_continuous():
        nonlocal continuous
        continuous = True
        perform_step()

    def perform_step():
        board.step()
        board.display()

        if continuous:
            # calls function in question after t milliseconds
            turtle.ontimer(perform_step, 25)

    # binds functions to the 's' and 'c' keys respectively
    turtle.onkey(step_once, 's')
    turtle.onkey(step_continuous, 'c')

    # prints out the coordinates (keys) of the current live cells
    def print_live():
        board.print_keys()

    turtle.onkey(print_live, 'p')
    
    # draws a Glider in the upper left of the display
    def draw_glider():
        board.glider()
        board.display()

    turtle.onkey(draw_glider, '1')

    # draws a Garden of Eden in the display
    def draw_garden():
        board.garden()
        board.display()

    turtle.onkey(draw_garden, '2')

    # draws a Gosper Glider Gun in the display
    def draw_glider_gun():
        board.glider_gun()
        board.display()

    turtle.onkey(draw_glider_gun, '3')

    # draws a Sparky in the display
    def draw_sparky():
        board.sparky()
        board.display()

    turtle.onkey(draw_sparky, '4')
        

    # turtle listens for key events
    turtle.listen()
    # required last statement in a program using turtle graphics
    turtle.mainloop()

main()
        
            
