import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 10))
def pol_reg(x_input, y_input, deg):
    l = []
    for x in x_input:
        tmp = []
        for j in range(0, deg + 1):
            tmp.append(x ** j)
        l.append(tmp)

    X = np.array(l, dtype=float)
    vector = np.array([[y] for y in y_input])
    coef = ((np.linalg.inv(X.T @ X)) @ X.T) @ vector

    x_axis = np.linspace(x_input[0], x_input[-1], 100)
    y_axis = []
    for z in x_axis:
        val = 0
        for i in range(len(coef)):
            val += coef[i][0] * z ** i
        y_axis.append(val)
    plt.plot(x_axis, y_axis, color='pink', linewidth = 5.0, label='poly reg')

def poly_fit(x_input, y_input, deg):
    coef = np.polyfit(x_input, y_input, deg)
    x_axis = np.linspace(x_input[0], x_input[-1], 100)
    y_axis = np.poly1d(coef)(x_axis)
    plt.plot(x_axis, y_axis, color='blue', label='polyfit class')


if __name__ == "__main__":
    x_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y_input = [3, 9, 7, -9, -10, -2, -10, -3, 8, 20]
    deg = 8
    pol_reg(x_input, y_input, deg)
    poly_fit(x_input, y_input, deg)
    plt.scatter(x_input, y_input, color='red', s=100, label='sample')
    plt.legend(loc='upper left', fontsize=18)
