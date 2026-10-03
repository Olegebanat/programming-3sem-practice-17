import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

STUDENT_NAME = "Yulian Mykhalchuk"
STUDENT_GROUP = "IT-42"

weeks = np.arange(1, 27)

conversion = np.array([
    2.1, 2.3, 2.2, 2.4, 2.3, 2.6, 2.5, 2.7, 2.6,
    2.8, 2.9, 2.7, 3.0, 3.1, 2.9, 3.2, 4.4, 3.3,
    3.2, 3.4, 3.5, 3.3, 3.6, 3.7, 3.5, 3.8
]) / 100

release_week = 12

fig, ax = plt.subplots(figsize=(9, 4))

ax.plot(
    weeks,
    conversion,
    marker="o"
)

ax.axvline(
    release_week,
    color="black",
    linestyle=":"
)

ax.text(
    release_week + 0.3,
    0.040,
    "new design"
)

ax.annotate(
    "promo",
    xy=(17, conversion[16]),
    xytext=(19, 0.044),
    arrowprops={"arrowstyle": "->"}
)

ax.set_title("Weekly conversion rate")
ax.set_xlabel("Week")
ax.set_ylabel("Conversion")

ax.set_xlim(0, 27)
ax.set_ylim(0.015, 0.05)

ax.yaxis.set_major_formatter(PercentFormatter(1.0))

ax.grid(True)

fig.text(
    0.01,
    0.01,
    f"{STUDENT_NAME}, {STUDENT_GROUP}",
    fontsize=8,
    color="gray"
)

fig.tight_layout(rect=[0, 0.03, 1, 1])
fig.savefig("task_5.png", dpi=150)

plt.show()