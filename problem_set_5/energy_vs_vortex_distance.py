import matplotlib.pyplot as plt
import numpy as np
import math
from xy_model import XYmodel

plot_model = XYmodel(20)
plot_model.place_vortex(5.5, 9.5, 1)
plot_model.place_vortex(13.5, 9.5, -1)
plot_model.plot("two_vortex_configuration")


system_size = 100
fixed_vortex_position = (10.5, 9.5)
vortex_distances = list(range(1, system_size - 12))
energies = []

for distance in vortex_distances:
    model = XYmodel(system_size)
    model.place_vortex(*fixed_vortex_position, 1)
    model.place_vortex(fixed_vortex_position[0] + distance, 9.5, -1)
    energies.append(model.compute_energy() - model.energy0)

fig, ax = plt.subplots()
ax.plot(vortex_distances, energies, label=r"$E_2(z_1, z_2) - E_0$")
ax.set(
    xlabel=r"Distance $d$",
    xscale="log"
)
ax.legend(loc="upper left")

fig.tight_layout()
fig.savefig("plots/energy_vs_vortex_distance")
