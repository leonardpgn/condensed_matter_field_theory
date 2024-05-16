import matplotlib.pyplot as plt
import numpy as np


class XYmodel:
    def __init__(self, n):
        self.dimension = n
        self.configuration = np.zeros((self.dimension, self.dimension))
        self.vortices = []
        self.energy0 = - 2 * (self.dimension - 1) ** 2

    def reset_configuration(self):
        self.vortices = []
        self.configuration = np.zeros((self.dimension, self.dimension))

    def place_vortex(self, x0, y0, winding_number=1):
        if x0 % 1 != .5 or y0 % 1 != .5:
            raise ValueError("vortex must be placed at center of plaquette!")
        if winding_number % 1 != 0:
            raise ValueError("Winding number must be integer!")

        self.vortices.append([x0, y0, winding_number])
        for x_pos in range(self.dimension):
            for y_pos in range(self.dimension):
                theta = np.arctan((y_pos - y0) / (x_pos - x0))
                if x_pos - x0 >= 0:
                    self.configuration[y_pos, x_pos] += winding_number * theta
                else:
                    self.configuration[y_pos, x_pos] += winding_number * (theta + np.pi)

    def quiver_data(self):
        x, y = np.arange(self.dimension), np.arange(self.dimension)
        u, v = np.zeros((self.dimension, self.dimension)), np.zeros((self.dimension, self.dimension))

        for x_pos in x:
            for y_pos in y:
                u[x_pos, y_pos] = np.cos(self.configuration[x_pos, y_pos])
                v[x_pos, y_pos] = np.sin(self.configuration[x_pos, y_pos])

        return x, y, u, v

    def plot(self, name=None):
        fig, ax = plt.subplots(dpi=500, figsize=(10, 10))
        ax.set(
            xticks=(0, self.dimension - 1),
            yticks=(0, self.dimension - 1),
            xticklabels=(1, self.dimension),
            yticklabels=(1, self.dimension),
            title=f"{self.dimension} x {self.dimension} square lattice; {len(self.vortices)} vortices"
        )
        ax.quiver(*self.quiver_data(), pivot="middle")
        if name is not None:
            fig.savefig(f'plots/{name}')
        else:
            fig.savefig(f'plots/plot_{self.dimension}dim_{len(self.vortices)}vortices')

    def compute_energy(self):
        energy = 0
        for x_pos in range(self.dimension - 1):
            for y_pos in range(self.dimension - 1):
                energy -= np.cos(self.configuration[x_pos, y_pos] - self.configuration[x_pos + 1, y_pos])
                energy -= np.cos(self.configuration[x_pos, y_pos] - self.configuration[x_pos, y_pos + 1])

        return energy


if __name__ == "__main__":
    model = XYmodel(20)
    model.place_vortex(9.5, 9.5, 1)
    model.plot()
