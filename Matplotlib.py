import numpy
import matplotlib.pyplot as plt

list_x = [1, 2, 3, 4, 5, 6, 7]
list_y = [x * 5 for x in list_x]

list_pl = plt.plot(list_x, list_y)
print(type(plt.plot(list_x, list_y)))

a = list_pl[0]
print(type(a))
print(dir("matplotlib.lines.Line2D"))


plt.show()
