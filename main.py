from tkinter import Tk, BOTH, Canvas
from window import *
from point import *
from maze import Maze


def main():
    win = Window(800,600)
    mazeA = Maze(10,10, 10, 10, 10,10, win)
    #mazeB = Maze(30,30, 5, 5, 30,30, win)
    mazeA._break_entrance_and_exit()
    #cellA = Cell(Point(100,100),Point(150,150), win)
    #cellA.draw(win.canvas, "red")
    win.wait_for_close()

main()
