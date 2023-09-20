from mediator import *

if __name__ == '__main__':
    heli = Helicopter()
    red = PlaneRed()
    blu = PlaneBlue()
    gre = PlaneGreen()
    mediator = Tower(heli, red, gre, blu)

    heli.launch()

    red.launch()

    heli.land()