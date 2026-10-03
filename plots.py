import numpy as np
import matplotlib.pyplot as plt

STUDENT_NAME = "Yulian Mykhalchuk"
STUDENT_GROUP = "IT-42"
N = 20

rng = np.random.default_rng(N)
x = np.linspace(-10, 10, 100)

y1 = x ** 2
y2 = N * x

fig, ax = plt.subplots()

ax.plot(x, y1, label="x^2")
ax.plot(x, y2, linestyle="--", label="N*x")

ax.set_title(f"{STUDENT_NAME}, {STUDENT_GROUP}")
ax.set_xlabel("x")
ax.set_ylabel("y")

ax.legend()
ax.grid(True)

fig.savefig("task_1.png", dpi=150)

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

temperature = [-3, -2, 3, 10, 16, 20, 22, 21, 16, 9, 3, -1]
average = np.mean(temperature)

fig, ax = plt.subplots()

ax.plot(range(12), temperature, marker="o", label="Temperature")
ax.axhline(average, linestyle="--", label="Average")

ax.set_xticks(range(12))
ax.set_xticklabels(months)

ax.set_title("Monthly temperature")
ax.set_xlabel("Month")
ax.set_ylabel("Temperature")

ax.legend()

fig.savefig("task_2.png", dpi=150)
categories = ["Sleep", "Study", "Games", "Sport", "Other"]
hours = [56, 30, 15, 8, 20]

fig, ax = plt.subplots()

bars = ax.barh(categories, hours)
ax.invert_yaxis()
ax.bar_label(bars)

ax.set_title("Weekly activities")
ax.set_xlabel("Hours")
ax.set_ylabel("Activity")

fig.savefig("task_3.png", dpi=150)
data = rng.normal(170 + N, 8, 1000)

mean_value = np.mean(data)
median_value = np.median(data)

fig, ax = plt.subplots()

ax.hist(data, bins=25)

ax.axvline(mean_value, color="red", label="Mean")
ax.axvline(median_value, color="green", label="Median")

ax.set_title("Height distribution")
ax.set_xlabel("Height")
ax.set_ylabel("Frequency")

ax.legend()

fig.savefig("task_4.png", dpi=150)
x = rng.uniform(0, 10, 50)
y = N + 3 * x + rng.normal(0, 4, 50)

mean_y = np.mean(y)
mask = y > mean_y

fig, ax = plt.subplots()

ax.scatter(x[mask], y[mask], color="red", marker="o", label="Above mean")
ax.scatter(x[~mask], y[~mask], color="blue", marker="x", label="Below mean")

ax.set_title("Scatter plot")
ax.set_xlabel("x")
ax.set_ylabel("y")

ax.legend()

fig.savefig("task_5.png", dpi=150)

correlation = np.corrcoef(x, y)[0, 1]
print(f"Correlation: {correlation:.2f}")
plt.show()