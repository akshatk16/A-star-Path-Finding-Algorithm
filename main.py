from logic import *


def main():
    end.show((0, 0, 0), 1)
    start.show((0, 0, 0), 1)
    if len(openSet) > 0:
        min_index = 0
        for i in range(len(openSet)):
            if openSet[i].f < openSet[min_index].f:
                min_index = i

        current = openSet[min_index]
        if current == end:
            print('done', current.f)
            start.show((0, 0, 0), 1)
            temp = current.f
            for i in range(round(current.f)):
                current.closed = False
                current.show((0,0,255), 0)
                current = current.previous
            end.show((0, 0, 0), 1)

            Tk().wm_withdraw()
            result = messagebox.askokcancel('Program Finished', ('The program finished!, \nShortest distance to the path is ' + str(temp) + ' blocks away. \n Would you like to try again?'))
            if result == True:
                os.execl(sys.executable,sys.executable, *sys.argv)
            else:
                ag = True
                while ag:
                    ev = pygame.event.get()
                    for event in ev:
                        if event.type == pygame.KEYDOWN:
                            ag = False
                            break
            pygame.quit()

        openSet.pop(min_index)
        closedSet.append(current)

        neighbours = current.neighbours
        for i in range(len(neighbours)):
            neighbor = neighbours[i]
            if neighbor not in closedSet:
                tempG = current.g + current.value
                if neighbor in openSet:
                    if neighbor.g > tempG:
                        neighbor.g = tempG
                else:
                    neighbor.g = tempG
                    openSet.append(neighbor)

            neighbor.h = heurisitic(neighbor, end)
            neighbor.f = neighbor.g + neighbor.h

            if neighbor.previous == None:
                neighbor.previous = current
    if var.get():
        for i in range(len(openSet)):
            openSet[i].show(green, 0)

        for i in range(len(closedSet)):
            if closedSet[i] != start:
                closedSet[i].show(red, 0)
    current.closed = True
