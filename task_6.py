import numpy as np
import matplotlib.pyplot as plt

STUDENT_NAME = "Yulian Mykhalchuk"
STUDENT_GROUP = "IT-42"

x = np.linspace(0, 4, 50)

fig, ax = plt.subplots(figsize=(7, 4))

ax.plot(
    x,
    x,
    color="black",
    linestyle="-",
    label="y = x"
)

ax.plot(
    x,
    x ** 2,
    color="black",
    linestyle="--",
    label="y = x^2"
)

ax.plot(
    x,
    x ** 3,
    color="black",
    linestyle=":",
    label="y = x^3"
)

ax.set_title("Print-friendly lines")
ax.set_xlabel("x")
ax.set_ylabel("y")

ax.set_xlim(0, 4)
ax.set_ylim(0, 65)

ax.grid(True, alpha=0.3)
ax.legend(loc="upper left")

fig.text(
    0.01,
    0.01,
    f"{STUDENT_NAME}, {STUDENT_GROUP}",
    fontsize=8,
    color="gray"
)

fig.tight_layout(rect=[0, 0.03, 1, 1])
fig.savefig("task_6.png", dpi=150)

plt.show()