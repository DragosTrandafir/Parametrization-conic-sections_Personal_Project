import matplotlib.pyplot as plt
import numpy as np
'''
importing the necessary libraries 
'''


def circle(xI,yI,r):
    '''
    Description: plots a circle through its geometrical parametrization
    Conditions: xI, yI, r - real numbers
    Input: param xI, param yI, param r
    Output: the plot
    '''
    fig, ax = plt.subplots()

    # defining the interval [0,2*pi]
    t= np.linspace(0,2*np.pi)
    radius = r

    # the coordinates of the points in parametrization of the circle
    x = radius*np.cos(t)+xI
    y = radius*np.sin(t)+yI

    # defining the ox, oy axes
    oX = np.linspace(-1000,1000)
    oY = np.linspace(0,0)

    # plotting the ox, oy axes and the actual circle
    plt.axis("equal")
    plt.plot(oX,oY,color="black")
    plt.plot(oY,oX,color="black")
    plt.plot(x, y, linewidth=3, color="red")

    # setting a certain width and length of the image ,so we can visualize everything,
    # and also plotting the center of the circle
    axes_range = 2 * radius
    ax.set(xlim=(xI - axes_range, xI + axes_range), ylim=(yI - axes_range, yI + axes_range))

    ax.scatter(xI, yI)
    plt.show()


def ellipse(xI,yI,a,b):
    '''
    Description: plots an ellipse through its geometrical parametrization
    Conditions: xI, yI, a, b - real numbers
    Input: param xI, param yI, param a, b
    Output: the plot
    '''
    fig, ax = plt.subplots()

    # defining the interval [0,2*pi]
    t= np.linspace(0,2*np.pi)

    # the coordinates of the points in parametrization of the ellipse
    x = a*np.cos(t)+xI
    y = b*np.sin(t)+yI

    # the parametrization assumes that a>b, so if it is not the case, we switch the values of these variables
    if b>a:
        a,b=b,a

    # defining the ox, oy axes
    oX = np.linspace(-1000,1000)
    oY = np.linspace(0,0)

    # plotting the ox, oy axes and the actual ellipse
    plt.axis("equal")
    plt.plot(oX,oY,color="black")
    plt.plot(oY,oX,color="black")
    plt.plot(x, y, linewidth=3, color="purple")

    # setting a certain width and length of the image ,so we can visualize everything,
    # and also plotting the center of the ellipse
    axes_range = 2 * a
    ax.set(xlim=(xI-axes_range, xI+axes_range),ylim=(yI-axes_range, yI+axes_range))
    ax.scatter(xI, yI)

    plt.show()


def hyperbola(xI,yI, a,b):
    '''
    Description: plots a hyperbola through its geometrical parametrization
    Conditions: xI, yI, a, b - real numbers
    Input: param xI, param yI, param a, b
    Output: the plot
    '''
    fig, ax = plt.subplots()

    # defining the intervals necessary for the parametrization
    t_array=[np.linspace(-100,-1.1,100),np.linspace(-0.9, 0.9, 100),np.linspace(1.1, 100, 100)]

    # defining the ox, oy axes
    oX = np.linspace(-50, 50)
    oY = np.linspace(0, 0)

    # plotting the ox, oy axes
    plt.axis("equal")
    plt.plot(oX, oY, color="black")
    plt.plot(oY, oX, color="black")

    # the coordinates of the points in parametrization of the hyperbola for every interval
    # and plotting the hyperbola on each interval
    for i in range(0,3):
        x = a * ((1+t_array[i]**2)/(1-t_array[i]**2)) + xI
        y = b * ((t_array[i]*2)/(1-t_array[i]**2)) + yI
        if a<b:
            x,y=y,x
        plt.plot(x, y, linewidth=3, color="pink")

    # setting a certain width and length of the image ,so we can visualize everything,
    # and also plotting the "center" of the hyperbola
    ax.set(xlim=(xI-20, xI+20),ylim=(yI-20, yI+20))
    ax.scatter(xI,yI)

    plt.show()


def parabola(xI,yI, a,ok):
    '''
    Description: plots a parabola through its geometrical parametrization
    Conditions: xI, yI, a - real numbers, ok - boolean value
    Input: param xI, param yI, param a, param ok
    Output: the plot
    '''
    fig, ax = plt.subplots()

    # defining a big interval so as to get a parametrization as accurate as possible
    t= np.linspace(-1000,1000,1000)

    # the coordinates of the points in parametrization of the parabola
    x = (t**2)/(4*a)
    y = t

    # defining the ox, oy axes
    oX = np.linspace(-50, 50)
    oY = np.linspace(0, 0)

    # plotting the ox, oy axes
    plt.plot(oX, oY, color="black")
    plt.plot(oY, oX, color="black")

    # we make a rotation of 90 deg anti-clockwise (if the parabola is of type 2) and a translation with the
    # vector corresponding to the peak
    if ok:
        plt.plot(y+xI, x+yI, linewidth=3, color="pink")
    else:
        plt.plot(x+xI, y+yI, linewidth=3, color="pink")

    # setting a certain width and length of the image ,so we can visualize everything
    ax.set(xlim=(xI - 40, xI + 40), ylim=(yI - 40, yI + 40))

    plt.show()





