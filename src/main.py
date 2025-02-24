from window import Window
from point import Point, Line
from cell import Cell





def main():
    win = Window(800, 600)

    #l = Line(Point(0,0), Point(800, 600))
    #l2 = Line(Point(0, 600), Point(800, 0))

    #win.draw_line(l, "RED")
    #win.draw_line(l2, "BLACK")
    c1 = Cell(Point(2, 2), Point(200, 200), win, right=False)
    c1.draw()
    c2 = Cell(Point(200, 300), Point(400, 500), win, left=False)
    c2.draw()
    c3 = Cell(Point(500, 500), Point(550, 550), win, top=False, bottom=False)
    c3.draw()
    c4 = Cell(Point(700, 10), Point(750, 60), win, left=False, right=False)
    c4.draw()

    c1.draw_move(c2)
    c3.draw_move(c4, undo=True)



    win.wait_for_close()



if __name__ == "__main__":
    main()