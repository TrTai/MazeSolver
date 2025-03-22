from tkinter import Canvas

class Point():
    def __init__(self, x, y):
        self._x = x
        self._y = y


class Line():
    
    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1._x, self.p1._y, self.p2._x, self.p2._y, fill = fill_color, width =2)


class Cell():

    def __init__(self,pointA, pointB, window = None) -> None:
        self._x1 = pointA._x
        self._y1 = pointA._y
        self._x2 = pointB._x
        self._y2 = pointB._y
        if self._x1 > self._x2 or self._y1 > self._y2:
            raise Exception("Invalid value")
        self.win = window
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True

    def draw(self, canvas, fill_color = "Black"):
        left_line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        top_line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        right_line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        bottom_line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        if self.left_wall:
            left_line.draw(canvas, fill_color)
        else:
            left_line.draw(canvas, "white")
        if self.top_wall:
            top_line.draw(canvas, fill_color)
        else:
            top_line.draw(canvas, "white")
        if self.right_wall:
            right_line.draw(canvas, fill_color)
        else:
            right_line.draw(canvas, "white")
        if self.bottom_wall:
            bottom_line.draw(canvas, fill_color)
        else:
            bottom_line.draw(canvas, "white")

    def draw_move(self, to_cell, undo = False):
        xSelf = (self._x1 + self._x2) /2
        ySelf = (self._y1 + self._y2) /2
        xNext = (to_cell._x1 + to_cell._x2) /2
        yNext = (to_cell._y1 + to_cell._y2) /2
        centerSelf = Point(xSelf, ySelf)
        centerNext = Point(xNext, yNext)
        progLine = Line(centerSelf, centerNext)
        if undo:
            progLine.draw(self.win.canvas, fill_color="gray")
        else:
            progLine.draw(self.win.canvas, fill_color="red")

