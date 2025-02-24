from window import Window
from point import Point, Line





def main():
    win = Window(800, 600)

    l = Line(Point(0,0), Point(800, 600))
    l2 = Line(Point(0, 600), Point(800, 0))

    win.draw_line(l, "RED")
    win.draw_line(l2, "BLACK")



    win.wait_for_close()



if __name__ == "__main__":
    main()