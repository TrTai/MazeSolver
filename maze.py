import time
from point import *
from cell import Cell
from window import *
from time import sleep
import random

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed is not None:
            self.seed = random.seed(seed)
        else:
            self.seed = random.random()
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
        if self.win is not None:
            for i in range(0, len(self._cells)):
                for j in range(0, len(self._cells[i])):
                    self._draw_cells(i,j)

    def _draw_cells(self,i,j):
        self._cells[i][j].draw(self.win.canvas)
        self._animate()
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._draw_cells(0,0)
        self._cells[self.num_cols -1][self.num_rows -1].bottom_wall = False
        self._draw_cells(self.num_cols -1, self.num_rows -1)

    def _break_walls_r(self, i, j):
        breakerCell = self._cells[i][j]
        breakerCell.visited = True
        neighborsi = [i + 1, i - 1]
        neighborsj = [j + 1, j - 1]
        while True:
            to_visit = []
            if i + 1 < self.num_cols and not self._cells[i+1][j].visited:
                to_visit.append((i+1, j))
            if i - 1 >= 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1, j))
            if j + 1 < self.num_rows and not self._cells[i][j+1].visited:
                to_visit.append((i, j+1))
            if j - 1 >= 0 and not self._cells[i][j-1].visited:
                to_visit.append((i, j-1))
            if len(to_visit) == 0:
                return
            print(f"to_visit: {to_visit}")
            randomSide = random.randint(0, len(to_visit) -1)
            nextCell = to_visit[randomSide]
            if nextCell == (i + 1, j) and not self._cells[i+1][j].visited:
                breakerCell.right_wall = False
                self._cells[i+1][j].left_wall = False
            elif nextCell == (i - 1, j) and not self._cells[i-1][j].visited:
                breakerCell.left_wall = False
                self._cells[i-1][j].right_wall = False
            elif nextCell == (i, j + 1) and not self._cells[i][j+1].visited:
                breakerCell.bottom_wall = False
                self._cells[i][j+1].top_wall = False
            elif nextCell == (i, j - 1) and not self._cells[i][j-1].visited:
                    breakerCell.top_wall = False
                    self._cells[i][j-1].bottom_wall = False
            print(f"Breaking wall to {nextCell}")
            self._draw_cells(i, j)
            #self._draw_cells(nextCell[0], nextCell[1])
            if not self._cells[nextCell[0]][nextCell[1]].visited:
                self._break_walls_r(nextCell[0], nextCell[1])
        
    def _reset_cells_visited(self):
        for i in range(0, len(self._cells)):
            for j in range(0, len(self._cells[i])):
                self._cells[i][j].visited = False
                self._draw_cells(i,j)

    def _solve(self):
        return self._solve_r(0,0)

    def _solve_r(self, i, j):
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        currentCell = self._cells[i][j]
        currentCell.visited = True
        print(f"walls at self._cells[{i},{j}]: Top:{currentCell.top_wall}, Bottom:{currentCell.bottom_wall}, Left:{currentCell.left_wall}, Right:{currentCell.right_wall}")
        self._animate()
        for d in range(0,4):
            if d == 0:
                print("Checking left")
                if i - 1 >= 0 and not self._cells[i-1][j].visited:
                    if not currentCell.left_wall:
                        currentCell.draw_move(self._cells[i-1][j])
                        print("open left")
                        if self._solve_r(i-1, j):
                            return True
                        else:
                            currentCell.draw_move(self._cells[i-1][j], undo = True)
            elif d == 1:
                print("Checking right")
                if i + 1 < self.num_cols and not self._cells[i+1][j].visited:
                    if not currentCell.right_wall:
                        currentCell.draw_move(self._cells[i+1][j])
                        print("open right")
                        if self._solve_r(i+1, j):
                            return True
                        else:
                            currentCell.draw_move(self._cells[i+1][j], undo = True)
            elif d == 2:
                print("Checking bottom")
                if j + 1 < self.num_rows and not self._cells[i][j+1].visited:
                    if not currentCell.bottom_wall:
                        currentCell.draw_move(self._cells[i][j+1])
                        print("open bottom")
                        if self._solve_r(i, j+1):
                            return True
                        else:
                            currentCell.draw_move(self._cells[i][j+1], undo = True)
            elif d == 3:
                print("Checking top")
                if j - 1 >= 0 and not self._cells[i][j-1].visited:
                    if not currentCell.top_wall:
                        currentCell.draw_move(self._cells[i][j-1])
                        print("open top")
                        if self._solve_r(i, j-1):
                            return True
                        else:
                            currentCell.draw_move(self._cells[i][j-1], undo = True)
        return False
