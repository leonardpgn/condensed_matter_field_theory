import matplotlib.pyplot as plt
import numpy as np
import math
from xy_model import XYmodel

system_sizes = np.logspace(1, 14, 30, base=2, dtype=int)
energies = []

for run, n in enumerate(system_sizes):
    model = XYmodel(n)
    model.place_vortex(math.floor(n/2) + .5, math.floor(n/2) + .5, 1)
    energies.append(model.compute_energy() - model.energy0)
    if run % 5 == 0:
        print(f"{run} / {len(system_sizes)}")

fig, ax = plt.subplots(dpi=500)
ax.plot(system_sizes, energies, label=r"One Vortex energy $E_1 - E_0$", alpha=.5)
ax.set(
    xlabel=r"System size $N$",
    xscale="log"
)
ax.legend(loc="upper left")

fig.tight_layout()
fig.savefig('plots/single_vortex_energies')

