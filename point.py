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


