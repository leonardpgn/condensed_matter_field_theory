import matplotlib.pyplot as plt
import numpy as np


class XYmodel:
    def __init__(self, n):
        self.dimension = n
        self.configuration = np.zeros((self.dimension, self.dimension))
        self.vortices = []

    def reset_configuration(self):
        self.vortices = []
        self.configuration = np.zeros((self.dimension, self.dimension))

    def place_vortex(self, x0, y0, winding_number=1):
        self.vortices.append([x0, y0, winding_number])
        for x_pos in range(self.dimension):
            for y_pos in range(self.dimension):
                theta = winding_number * np.arctan((y_pos - y0) / (x_pos - x0))
                if x_pos - x0 >= 0:
                    self.configuration[y_pos, x_pos] = theta
                else:
                    self.configuration[y_pos, x_pos] = theta + np.pi

    def quiver_data(self):
        x, y = np.arange(self.dimension), np.arange(self.dimension)
        u, v = np.zeros((self.dimension, self.dimension)), np.zeros((self.dimension, self.dimension))

        for x_pos in x:
            for y_pos in y:
                u[x_pos, y_pos] = np.cos(self.configuration[x_pos, y_pos])
                v[x_pos, y_pos] = np.sin(self.configuration[x_pos, y_pos])

        return x, y, u, v

    def plot(self):
        fig, ax = plt.subplots(dpi=500)
        ax.quiver(*self.quiver_data(), pivot="middle")
        fig.savefig(f'plots/plot_{self.dimension}dim_{len(self.vortices)}vortices')


model = XYmodel(10)
model.place_vortex(5.5, 5.5)
model.plot()
print(model.configuration)
