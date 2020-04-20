from math import sqrt
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
from cell import *

pygame.display.set_caption('A* Path Finding Algorithm')

for i in range(cols):
    grid[i] = [0 for i in range(row)]  # create 2D array

for i in range(cols):
    for j in range(row):
        grid[i][j] = cell(i, j)


start = grid[12][5]
end = grid[3][6]

for i in range(cols):
    for j in range(row):
        grid[i][j].show((255, 0, 255), 1)  # display grid

for i in range(0, row):
    grid[0][i].show(grey, 0)
    grid[0][i].obs = True
    grid[cols - 1][i].obs = True
    grid[cols - 1][i].show(grey, 0)
    grid[i][row - 1].show(grey, 0)
    grid[i][0].show(grey, 0)
    grid[i][0].obs = True
    grid[i][row - 1].obs = True


def onsubmit():
    global start
    global end
    st = startBox.get().split(',')
    ed = endBox.get().split(',')
    start = grid[int(st[0])][int(st[1])]
    end = grid[int(ed[0])][int(ed[1])]
    window.quit()
    window.destroy()

window = Tk()
window.title("Source and Target for Path")
label = Label(window, text='Enter starting coordinates as x, y: ')
startBox = Entry(window)
label1 = Label(window, text='Enter ending coordinates as x, y: ')
endBox = Entry(window)
var = IntVar()
showPath = ttk.Checkbutton(window, text='Show Steps? ', onvalue=1, offvalue=0, variable=var)

submit = Button(window, text='Submit', command = onsubmit)

showPath.grid(columnspan=2, row=2)
submit.grid(columnspan=2, row=3)
label1.grid(row=1, pady=3)
endBox.grid(row=1, column=1, pady=3)
startBox.grid(row=0, column=1, pady=3)
label.grid(row=0, pady=3)

window.update()
mainloop()

pygame.init()
openSet.append(start)


def mousePress(x):
    t = x[0]
    w = x[1]
    g1 = t // (640 // cols)
    g2 = w // (640 // row)
    wall = grid[g1][g2]
    if wall != start and wall != end:
        if wall.obs == False:
            wall.obs = True
            wall.show((255, 255, 255), 0)


end.show((0, 0, 255), 0)
start.show((0, 0, 255), 0)

loop = True
while loop:
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.QUIT:
            pygame.quit()
        if pygame.mouse.get_pressed()[0]:
            try:
                pos = pygame.mouse.get_pos()
                mousePress(pos)
            except AttributeError:
                pass
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                loop = False
                break


for i in range(cols):
    for j in range(row):
        grid[i][j].addneighbours(grid)


def heurisitic(n, e):
    d = sqrt((n.i - e.i)**2 + (n.j - e.j)**2)  # distance
    return d
