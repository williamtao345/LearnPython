import numpy as np
import matplotlib.pyplot as plt


def step_function(input_x):
    return np.array(input_x > 0, dtype=int)


def sigmoid_function(input_x):
    return 1 / (1 + np.exp(-input_x))


def relu(input_x):
    return np.maximum(0, input_x)


def softmax(input_x):
    c = np.max(input_x)
    exp_x = np.exp(input_x - c)
    exp_sum = np.sum(exp_x)
    return exp_x / exp_sum


x = np.arange(-10, 10, 0.1)
y1 = step_function(x)
y2 = sigmoid_function(x)

plt.plot(x, y1, linestyle="--")
plt.plot(x, y2)

plt.ylim(-0.1, 1.1)
plt.show()
