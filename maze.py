import time
from point import *
from window import *
from time import sleep


class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        i = self.x1
        for col in range(self.num_cols):
            colList = []
            j = self.y1
            for row in range(self.num_rows):
                pointA = Point(i, j)
                j += self.cell_size_y
                pointB = Point(i + self.cell_size_x, j)
                colList.append(Cell(pointA, pointB, self.win))
            self._cells.append(colList)
            i += self.cell_size_x
        for i in range(0, len(self._cells)):
            for j in range(0, len(self._cells[i])):
                self._draw_cells(i,j)

    def _draw_cells(self,i,j):
        self._cells[i][j].draw(self.win.canvas)
        self._animate()
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.1)

    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._draw_cells(0,0)
        self._cells[self.num_cols -1][self.num_rows -1].bottom_wall = False
        self._draw_cells(self.num_cols -1, self.num_rows -1)
