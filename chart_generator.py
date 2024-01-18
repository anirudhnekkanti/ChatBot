import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

def generate_bar_chart():
    labels = ['Category A', 'Category B', 'Category C']
    values = [30, 45, 25]

    # Adjust the figsize parameter to set the width and height of the figure
    fig, ax = plt.subplots(figsize=(8, 6))

    ax.bar(labels, values)
    ax.set_ylabel('Values')
    ax.set_title('Bar Chart Example')

    # Save the chart to an image file
    chart_filename = 'chart.png'
    plt.savefig(chart_filename)

    return chart_filename

if __name__ == "__main__":
    generate_bar_chart()
