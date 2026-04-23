import random
import matplotlib.pyplot as plt
from operator import index, indexOf


def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(seznam):
    seznam = seznam.copy()
    for i in range(len(seznam)):
        min_index = i
        for x in range(i, len(seznam)):
            if seznam[x] < seznam[min_index]:
                min_index = x
        seznam[i], seznam[min_index] = seznam[min_index], seznam[i]
    return seznam



def bubble_sort(seznam):
    seznam=seznam.copy()

    plt.ion()
    plt.show()

    for i in range(len(seznam)-1):
        for x in range(len(seznam)-1):
            if seznam[x] > seznam [x+1]:
                seznam[x+1], seznam[x] = seznam[x], seznam[x+1]
            index_highlight1 = x
            index_highlight2 = x + 1
            colors = ["steelblue"] * len(seznam)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(seznam)), seznam, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)

    plt.ioff()
    plt.show()

    return seznam


if __name__ == "__main__":
    values = random_numbers(5)
    print(values)
    selekce = selection_sort(values)
    print(selekce)
    bubble=bubble_sort(values)
    print(bubble)

    # small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20