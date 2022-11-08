%% FOR PLOTS IN LATEX

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})
matplotlib.style.use("classic")

fig = plt.figure(facecolor="white", figsize=(5, 5), constrained_layout=True)
fig.set_size_inches(w=3.5, h=3.5)
plt.plot(x, y, label=r"$y$", linestyle="-", color="k")
plt.xlabel(r"$x$", fontsize=18)
plt.ylabel(r"$y$", fontsize=18)
plt.legend(frameon=False, fontsize="small", loc="center right")
plt.savefig("fig.pgf")
