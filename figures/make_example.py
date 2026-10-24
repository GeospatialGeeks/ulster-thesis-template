"""Draws the example figure, saved twice: PDF for the PDF build and PNG for the Word build.

    python figures/make_example.py

Save every figure in both formats under the same name, as here, so that the two versions of the thesis match.
"""
import pathlib
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = pathlib.Path(__file__).resolve().parent
plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"], "font.size": 10})

x = np.linspace(0, 10, 200)
fig, ax = plt.subplots(figsize=(5.5, 3.2))
ax.plot(x, np.sin(x), color="#1f4e79", lw=2)
ax.set_xlabel("x")
ax.set_ylabel("sin(x)")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
for ext in ("pdf", "png"):
    fig.savefig(HERE / f"thesis-example-figure.{ext}", dpi=300)
