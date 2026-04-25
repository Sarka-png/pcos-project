import matplotlib.pyplot as plt

factors = ["Menstrual", "Exercise", "Caffeine", "Mental"]
values = [37, 22, 59, 51]

plt.figure()
plt.bar(factors, values)
plt.title("PCOS Risk Factors Comparison")
plt.xlabel("Factors")
plt.ylabel("Values")

plt.savefig("bar_chart.png")
plt.show()
plt.grid(axis='y', linestyle='--', alpha=0.7)
