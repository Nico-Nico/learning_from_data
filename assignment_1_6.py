import random
import numpy as np
import matplotlib.pyplot as plt

N = 100  # size of data set


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + ", " + str(self.y)

    def what_side_of_line(self, line):
        d = (self.x-line.p1.x) * (line.p2.y-self.y) - \
            (self.y-line.p1.y) * (line.p2.x-self.x)
        if d > 0:
            return 1
        else:
            return -1


class Line:
    """docstring for Line"""
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return "This line goes through the points " + \
            "(" + str(self.p1.x) + ", " + str(self.p1.y) + ") " + \
            "and " + \
            "(" + str(self.p2.x) + ", " + str(self.p2.y) + ")."


def target(x, y, p1, p2):
    d = (x-p1.x)*(p2.y-p1.y) - (y-p1.y)*(p2.x-p1.x)
    if d > 0:
        return 1
    else:
        return -1

target_function = Line(Point(random.uniform(-1, 1), random.uniform(-1, 1)),
                       Point(random.uniform(-1, 1), random.uniform(-1, 1)))

training_points = [Point(random.uniform(-1, 1), random.uniform(-1, 1)) for i in range(N)]
training_set = [(point, point.what_side_of_line(target_function)) for point in training_points]

# plotting data points
x_neg = [p.x for p in training_points if p.what_side_of_line(target_function) == -1]
y_neg = [p.y for p in training_points if p.what_side_of_line(target_function) == -1]
x_pos = [p.x for p in training_points if p.what_side_of_line(target_function) == 1]
y_pos = [p.y for p in training_points if p.what_side_of_line(target_function) == 1]
plt.plot(x_neg, y_neg, 'r.')
plt.plot(x_pos, y_pos, 'g.')

# line function from two points: y - y_1 = \frac{y_2 - y_1}{x_2 - x_1} (x - x_1)
x1, y1, x2, y2 = target_function.p1.x, target_function.p1.y, target_function.p2.x, target_function.p2.y
x = np.linspace(-1, 1)
y = (x-x1)*(y2-y1)/(x2-x1) + y1
plt.plot(x, y, 'b')
plt.axis([-1, 1, -1, 1])

plt.xlabel('x')
plt.ylabel('y')
plt.title("Interesting title")
plt.legend()

plt.show()
