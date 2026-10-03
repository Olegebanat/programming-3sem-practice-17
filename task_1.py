import numpy as np
import matplotlib.pyplot as plt

STUDENT_NAME = "Yulian Mykhalchuk"
STUDENT_GROUP = "IT-42"

n = np.arange(1, 31)

y1 = n
y2 = n * np.log(n)
y3 = n ** 2
y4 = 2 ** n

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.plot(n, y1, label="O(n)")
ax1.plot(n, y2, label="O(n log n)")
ax1.plot(n, y3, label="O(n^2)")
ax1.plot(n, y4, label="O(2^n)")

ax1.set_title("Linear scale")
ax1.set_xlabel("n")
ax1.set_ylabel("Operations")
ax1.set_ylim(0, 1000)
ax1.grid(True, alpha=0.3)

ax2.plot(n, y1, label="O(n)")
ax2.plot(n, y2, label="O(n log n)")
ax2.plot(n, y3, label="O(n^2)")
ax2.plot(n, y4, label="O(2^n)")

ax2.set_title("Log scale")
ax2.set_xlabel("n")
ax2.set_ylabel("Operations")
ax2.set_yscale("log")
ax2.grid(True, alpha=0.3)

handles, labels = ax1.get_legend_handles_labels()
fig.legend(handles, labels, loc="upper center", ncol=4)

fig.text(
    0.01, 0.01,
    f"{STUDENT_NAME}, {STUDENT_GROUP}",
    fontsize=8,
    color="gray"
)

fig.tight_layout(rect=[0, 0.03, 1, 0.93])
fig.savefig("task_1.png", dpi=150)

plt.show()