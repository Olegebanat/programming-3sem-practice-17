import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

STUDENT_NAME = "Yulian Mykhalchuk"
STUDENT_GROUP = "IT-42"

rng = np.random.default_rng(38)

dates = pd.date_range("2025-08-01", periods=120, freq="D")
day = np.arange(120)

visits = 500 + 5 * day + rng.normal(0, 60, size=120)
visits[dates.dayofweek >= 5] *= 0.6

visits[40:45] = np.nan

series = pd.Series(visits, index=dates)
mean_7 = series.rolling(window=7, min_periods=4).mean()

fig, ax = plt.subplots(figsize=(10, 4))

ax.plot(dates, visits, linewidth=0.8, alpha=0.5, label="daily")
ax.plot(dates, mean_7, linewidth=2.5, label="7-day mean")

ax.axvspan(
    dates[40],
    dates[44],
    color="red",
    alpha=0.1
)

ax.text(
    dates[42],
    250,
    "server down",
    color="red",
    ha="center"
)

ax.set_title("Site visits")
ax.set_ylabel("Visitors per day")

ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b"))

ax.set_xlim(dates[0], dates[-1])
ax.set_ylim(0, 1230)

ax.grid(True, alpha=0.3)
ax.legend(loc="lower right")

fig.text(
    0.01,
    0.01,
    f"{STUDENT_NAME}, {STUDENT_GROUP}",
    fontsize=8,
    color="gray"
)

fig.text(0.995, 0.01, "2025", ha="right")

fig.tight_layout(rect=[0, 0.03, 1, 1])
fig.savefig("task_2.png", dpi=150)

plt.show()