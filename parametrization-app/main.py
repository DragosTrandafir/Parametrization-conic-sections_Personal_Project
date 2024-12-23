import matplotlib.pyplot as plt
from figure_repo import figures

circle_option = 1
ellipse_option = 2
hyperbola_option = 3
parabola_type1_option = 4
parabola_type2_option = 5
stop_option = 6

fig, ax = plt.subplots()
plt.figure(figsize=(12, 8))


def print_menu():
    menu_string = ""
    menu_string += (f"MENU\n\tPlot:\n\t\t{circle_option}. Circle\n" +
                    f"\t\t{ellipse_option}. Ellipse\n\t\t{hyperbola_option}. Hyperbola\n\t\t{parabola_type1_option}. Parabola1 (of the form y^2=4ax)\n\t"
                    + f"\t{parabola_type2_option}. Parabola2 (of the form y=4ax^2)\n\t\t{stop_option}. Stop ")
    return menu_string


'''
in the menu, we are able to chose options and plot the wanted figure
'''

start = False
while not start:
    print(print_menu())
    figure_type = int(input("Read a type of figure: "))
    if figure_type == circle_option:
        xI = float(input("X coordinate of center: "))
        yI = float(input("Y coordinate of center: "))
        r = float(input("Radius : "))
        figures.circle(xI, yI, r)
    elif figure_type == ellipse_option:
        xI = float(input("X coordinate of center: "))
        yI = float(input("Y coordinate of center: "))
        a = float(input("Size of semi-major axis : "))
        b = float(input("Size of semi-minor axis : "))
        figures.ellipse(xI, yI, a, b)
    elif figure_type == hyperbola_option:
        xI = float(input("X coordinate of center: "))
        yI = float(input("Y coordinate of center: "))
        a = float(input("Size of semi-major axis : "))
        b = float(input("Size of semi-minor axis : "))
        figures.hyperbola(xI, yI, a, b)
    elif figure_type == parabola_type1_option:
        xI = float(input("X coordinate of center: "))
        yI = float(input("Y coordinate of center: "))
        a = float(input("Size of semi-major axis : "))
        ok = False
        figures.parabola(xI, yI, a, ok)
    elif figure_type == parabola_type2_option:
        xI = float(input("X coordinate of center: "))
        yI = float(input("Y coordinate of center: "))
        a = float(input("Size of semi-major axis : "))
        ok = True
        figures.parabola(xI, yI, a, ok)
    elif figure_type == stop_option:
        start = True
    else:
        print("Not an available option!")
