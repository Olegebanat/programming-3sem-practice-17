import numpy as np
import matplotlib.pyplot as plt

STUDENT_NAME = "Yulian Mykhalchuk"
STUDENT_GROUP = "IT-42"

tariff_months = [1, 5, 10, 12]
tariff_prices = [2.64, 4.32, 4.80, 4.80]

months = np.arange(1, 13)
usage = np.array([285, 262, 231, 198, 160, 131, 118, 126, 158, 205, 247, 279])
norm = 200

fig, (ax1, ax2) = plt.subplots(
    2, 1,
    figsize=(8, 6),
    sharex=True,
    gridspec_kw={"height_ratios": [1, 2]}
)

ax1.step(
    tariff_months,
    tariff_prices,
    where="post",
    color="black"
)
ax1.plot(
    tariff_months,
    tariff_prices,
    "o",
    color="black"
)

ax1.set_title("Electricity tariff, per kWh")
ax1.set_ylabel("Price")
ax1.set_ylim(2.0, 5.3)
ax1.set_yticks([2, 3, 4, 5])
ax1.set_yticklabels(["2.00 UAH", "3.00 UAH", "4.00 UAH", "5.00 UAH"])
ax1.grid(True, alpha=0.3)

ax2.plot(
    months,
    usage,
    color="black",
    marker="o",
    label="usage"
)

ax2.axhline(
    norm,
    color="gray",
    linestyle="--",
    label="norm"
)

ax2.fill_between(
    months,
    usage,
    norm,
    where=usage > norm,
    color="red",
    alpha=0.3,
    label="over norm"
)

ax2.fill_between(
    months,
    usage,
    norm,
    where=usage <= norm,
    color="green",
    alpha=0.3,
    label="under norm"
)

ax2.set_title("Monthly usage")
ax2.set_xlabel("Month")
ax2.set_ylabel("Usage, kWh")
ax2.set_xticks(months)
ax2.set_ylim(100, 320)
ax2.grid(True, alpha=0.3)

ax2.legend(
    loc="upper center",
    ncol=4
)

fig.text(
    0.01,
    0.01,
    f"{STUDENT_NAME}, {STUDENT_GROUP}",
    fontsize=8,
    color="gray"
)

fig.tight_layout(rect=[0, 0.03, 1, 1])
fig.savefig("task_3.png", dpi=150)

plt.show()