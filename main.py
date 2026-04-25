import matplotlib.pyplot as plt

def plot_chart(title, labels, values, filename):
    plt.figure()
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title(title)
    plt.savefig(filename)
    plt.close()

def main():
    # 1. Menstrual Status
    plot_chart(
        "Menstrual Status",
        ["Normal", "Irregular", "Extreme", "No Periods"],
        [32, 37, 18, 13],
        "menstrual_chart.png"
    )

    # 2. Physical Exercise
    plot_chart(
        "Physical Exercise",
        ["Walking", "Yoga", "No Exercise", "Gym"],
        [49, 19, 22, 10],
        "exercise_chart.png"
    )

    # 3. Caffeine Intake
    plot_chart(
        "Caffeine Consumption",
        ["Daily", "Sometimes", "Never"],
        [59, 24, 17],
        "caffeine_chart.png"
    )

    # 4. Mental Health
    plot_chart(
        "Mental Health",
        ["Yes", "No"],
        [51, 49],
        "mental_chart.png"
    )

    print("All charts generated successfully!")

if __name__ == "__main__":
    main()