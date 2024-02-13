import matplotlib.pyplot as plt
from figure_repo import figures

fig, ax = plt.subplots()
plt.figure(figsize=(12, 8))


def print_menu():
    s=""
    s+=("MENU\n\tPlot:\n\t\t1. Circle\n"
        "\t\t2. Ellipse\n\t\t3. Hyperbola\n\t\t4. Parabola1 (of the form y^2=4ax)\n\t"
        "\t5. Parabola2 (of the form y=4ax^2)\n\t\t6. Stop ")
    return s


'''
in the menu, we are able to chose options and plot the wanted figure
'''

start=False
while not start:
    print(print_menu())
    figure_type=input("Read a type of figure: ")
    if figure_type=="1":
        xI= float(input("X coordinate of center: "))
        yI = float(input("Y coordinate of center: "))
        r = float(input("Radius : "))
        figures.circle(xI, yI, r)
    elif figure_type=="2":
        xI=float(input("X coordinate of center: "))
        yI = float(input("Y coordinate of center: "))
        a = float(input("Size of semi-major axis : "))
        b = float(input("Size of semi-minor axis : "))
        figures.ellipse(xI, yI, a, b)
    elif figure_type=="3":
        xI=float(input("X coordinate of center: "))
        yI = float(input("Y coordinate of center: "))
        a = float(input("Size of semi-major axis : "))
        b = float(input("Size of semi-minor axis : "))
        figures.hyperbola(xI,yI, a,b)
    elif figure_type=="4":
        xI=float(input("X coordinate of center: "))
        yI = float(input("Y coordinate of center: "))
        a = float(input("Size of semi-major axis : "))
        ok=False
        figures.parabola(xI, yI, a,ok)
    elif figure_type=="5":
        xI=float(input("X coordinate of center: "))
        yI = float(input("Y coordinate of center: "))
        a = float(input("Size of semi-major axis : "))
        ok=True
        figures.parabola(xI, yI, a,ok)
    elif figure_type=="6":
        start = True
    else:
        print("Not an available option!")
