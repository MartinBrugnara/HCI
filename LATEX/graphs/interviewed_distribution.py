#!/usr/local/bin/python

import numpy as np
import matplotlib.pyplot as plt

def plot():
    labels = ['Stud. informatica', 'Stud. altri atenei', 'Altre professioni']
    sizes = [8, 3, 1]
    colors = ['yellowgreen', 'gold', 'lightskyblue']
    explode = (0.1, 0, 0)

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                    autopct='%1.1f%%', shadow=True, startangle=240)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    plt.show()


    labels = ['Si', 'No']
    sizes = [2,6]
    colors = ['#FFAB91', '#AB47BC']
    explode = (0.05, 0.05)

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                    autopct='%1.1f%%', shadow=True, startangle=90)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    plt.show()






if __name__ == '__main__':
    plot()
