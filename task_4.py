import matplotlib.pyplot as plt

STUDENT_NAME = "Yulian Mykhalchuk"
STUDENT_GROUP = "IT-42"

cities = {
    "Kyiv": [-3.5, -2.4, 2.1, 9.4, 15.6, 19.0, 20.8, 20.0, 14.8, 8.6, 2.7, -1.6],
    "Lviv": [-2.9, -1.8, 2.3, 8.3, 13.6, 16.6, 18.2, 17.6, 13.2, 8.3, 3.3, -1.1],
    "Odesa": [-0.9, -0.3, 3.4, 9.3, 15.5, 20.0, 22.8, 22.4, 17.3, 11.5, 5.9, 1.3],
    "Kharkiv": [-5.5, -4.9, 0.1, 8.4, 15.2, 18.8, 20.9, 20.0, 14.1, 7.6, 1.2, -3.1],
    "Dnipro": [-3.9, -3.2, 1.8, 10.1, 16.5, 20.2, 22.5, 21.8, 16.0, 9.0, 2.5, -1.8],
    "Uzhhorod": [-1.9, 0.1, 5.2, 11.2, 16.1, 19.4, 21.1, 20.6, 15.8, 10.2, 4.5, -0.3],
}

months = list(range(1, 13))

month_names = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 8))

order = ["Odesa", "Dnipro", "Uzhhorod", "Kharkiv", "Kyiv", "Lviv"]

for city in order:
    ax1.plot(months, cities[city], label=city)

ax1.set_title("Six cities")
ax1.set_ylabel("Temperature, C")
ax1.set_xticks(months)
ax1.set_xticklabels(month_names)
ax1.grid(True, alpha=0.3)

ax1.legend(
    title="City",
    loc="upper left",
    bbox_to_anchor=(1.02, 1)
)

selected = ["Odesa", "Kyiv", "Lviv"]

for city in selected:
    ax2.plot(months, cities[city])

ax2.set_title("Three cities")
ax2.set_xlabel("Month")
ax2.set_ylabel("Temperature, C")
ax2.set_xticks(months)
ax2.set_xticklabels(month_names)
ax2.grid(True, alpha=0.3)

for city in selected:
    ax2.text(
        12.15,
        cities[city][-1],
        city
    )

max_temp = max(cities["Odesa"])
max_month = cities["Odesa"].index(max_temp) + 1

ax2.annotate(
    "max 22.8 C",
    xy=(max_month, max_temp),
    xytext=(9, 24),
    arrowprops={"arrowstyle": "->"}
)

fig.text(
    0.01,
    0.01,
    f"{STUDENT_NAME}, {STUDENT_GROUP}",
    fontsize=8,
    color="gray"
)

fig.tight_layout(rect=[0, 0.03, 0.9, 1])
fig.savefig("task_4.png", dpi=150)

plt.show()