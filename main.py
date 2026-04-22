import matplotlib.pyplot as plt

categories = ["Daily", "Sometimes", "Never"]
counts = [7, 85, 8]

plt.figure()
plt.pie(counts, labels=categories, autopct='%1.1f%%')
plt.title("PCOS Distribution")

plt.savefig("pie_chart.png")
plt.show()
