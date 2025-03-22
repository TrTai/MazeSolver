from tkinter import Tk, BOTH, Canvas
from point import Line

class Window():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Maze Mapper")
        self.canvas = Canvas()
        self.canvas.pack()
        self.isRunning = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update()
        self.root.update_idletasks

    def wait_for_close(self):
        self.isRunning = True
        while self.isRunning == True:
            self.redraw()

    def close(self):
        self.isRunning = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

