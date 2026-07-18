

from data_preprocess import processdata
import matplotlib.pyplot as plt

def plot_candy_counts(candy_rows):
    labels = list(candy_rows.keys())
    sizes = [len(rows) for rows in candy_rows.values()]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.set_title('Number of Samples per Candy')
    plt.show()


candy_rows = processdata()
plot_candy_counts(candy_rows)